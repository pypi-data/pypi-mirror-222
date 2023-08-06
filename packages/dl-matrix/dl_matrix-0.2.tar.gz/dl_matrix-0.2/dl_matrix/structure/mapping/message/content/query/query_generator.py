from typing import List, Dict
from pydantic import BaseModel, Field
from scipy.spatial.distance import cosine
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForMaskedLM
from sentence_transformers import SentenceTransformer
import torch
import random
import logging
import numpy as np
import spacy
from spacy.lang.en import English
import openai


OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY


class QueryGenerator(BaseModel):
    """
    A class for generating creative prompts using a combination of linguistic analysis
    and phrase synthesis.
    """

    keywords: List[str] = Field(...)

    min_keywords: int = Field(
        1, description="Minimum number of keywords to use in each prompt."
    )
    max_keywords: int = Field(
        3, description="Maximum number of keywords to use in each prompt."
    )
    phrase_ratio: float = Field(
        0.5, description="Ratio of new phrases to include in each prompt."
    )

    class Config:
        arbitrary_types_allowed = True

    # Initialize the transformers pipeline for text generation and BERT model for scoring.
    generator = pipeline("text-generation", model="gpt2")
    tokenizer: AutoTokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    model: AutoModelForMaskedLM = AutoModelForMaskedLM.from_pretrained(
        "distilbert-base-uncased"
    )
    nlp = spacy.load("en_core_web_md")

    embedding_generator: SentenceTransformer = SentenceTransformer("all-mpnet-base-v2")

    adjectives = ["creative", "innovative", "unusual", "surprising", "unique"]
    adverbs = ["quickly", "efficiently", "surprisingly", "exceptionally", "creatively"]

    def add_keyword(self, keyword: str) -> None:
        """Add a new keyword to the list."""
        self.keywords.append(keyword)

    def remove_keyword(self, keyword: str) -> None:
        """Remove a keyword from the list."""
        self.keywords.remove(keyword)

    def synthesize_new_word_or_phrase(self) -> str:
        """Generate a new word or phrase by randomly combining keywords."""
        num_keywords = random.randint(self.min_keywords, self.max_keywords)
        keywords = random.sample(self.keywords, num_keywords)
        new_word = "".join(
            [
                random.choice(self.adjectives),
                random.choice(keywords),
                random.choice(self.adverbs),
            ]
        )
        return new_word

    def generate_new_prompt(
        self, template: str, context: str = "", prompt_keywords: List[str] = None
    ) -> str:
        """
        Generate a new prompt by randomly injecting synthesized words or phrases into the template.
        This method now supports a context argument, which can help generate more contextually relevant prompts.
        It also supports an optional prompt_keywords argument, which will preferentially use these keywords.
        """
        placeholder_count = template.count("{}")
        num_keywords = max(self.min_keywords, min(self.max_keywords, placeholder_count))

        new_keywords = []
        if context:
            prompt = self.generator(
                context, max_new_tokens=num_keywords, do_sample=True
            )
            new_keywords += prompt[0]["generated_text"].split()[-num_keywords:]
        if prompt_keywords:
            new_keywords += random.sample(
                prompt_keywords, min(num_keywords, len(prompt_keywords))
            )
        while len(new_keywords) < num_keywords:
            if random.random() < self.phrase_ratio:
                new_keywords.append(self.synthesize_new_word_or_phrase())
            else:
                # Generate context-related keyword
                if context and random.random() < 0.5:
                    keyword_prompt = (
                        openai.Completion.create(
                            engine="text-davinci-003",
                            prompt=context,
                            temperature=0.3,
                            max_new_tokens=20,
                        )
                        .choices[0]
                        .text.strip()
                    )
                    new_keywords.append(keyword_prompt)
                else:
                    new_keywords.append(random.choice(self.keywords))
        random.shuffle(new_keywords)  # Randomize the order of keywords
        return template.format(*new_keywords)

    def generate_expressive_prompts(
        self,
        templates: List[str],
        num_prompts: int = 10,
        user_profile: dict = None,
        context: str = "",
        prompt_keywords: Dict[str, List[str]] = None,
    ) -> List[str]:
        """
        Generate a list of expressive prompts by repeatedly applying the generate_new_prompt method on a list of templates.
        The prompts can be personalized based on a user profile.
        """
        prompts = []
        for _ in range(num_prompts):
            template = random.choice(templates)  # Randomly select a template
            if user_profile:
                # Personalize template selection and keyword generation
                prompts.append(
                    self.generate_new_prompt(
                        template, context, prompt_keywords, user_profile
                    )
                )
            else:
                prompts.append(
                    self.generate_new_prompt(template, context, prompt_keywords)
                )
        return prompts

    def generate_new_prompt_with_context(
        self, context: str, user_profile: dict = None
    ) -> str:
        """Generate a new prompt based on a given context and a user profile."""
        try:
            # If a user profile is provided, personalize the prompt generation
            if user_profile:
                output = self.personalized_generator(
                    context, user_profile, max_new_tokens=20, do_sample=True
                )
            else:
                output = self.generator(context, max_new_tokens=20, do_sample=True)
            return output[0]["generated_text"]
        except Exception as e:
            logging.error(f"Error generating prompt with context: {str(e)}")
            return ""

    def personalized_generator(
        self, context: str, user_profile: dict, max_new_tokens: int, do_sample: bool
    ) -> str:
        """
        Generate a new prompt based on a given context and a user profile.
        """
        # Extract user interests from the user profile
        user_interests = user_profile.get("interests", [])

        # Use the user's interests to generate context-specific keywords
        context_keywords = self.generate_keywords_from_interests(
            context, user_interests
        )

        # Add these context-specific keywords to the regular keyword generation
        keywords = (
            self.generate_keywords(context, max_new_tokens, do_sample)
            + context_keywords
        )

        # Generate a new prompt using these keywords
        prompt = self.generate_prompt_from_keywords(keywords)

        return prompt

    def generate_keywords_from_interests(self, interests: List[str]) -> List[str]:
        keywords = []
        for interest in interests:
            doc = self.nlp(interest)
            for ent in doc.ents:
                keywords.append(ent.text)
        return keywords

    def generate_keywords(self, context: str) -> List[str]:
        keywords = []
        doc = self.nlp(context)
        for ent in doc.ents:
            keywords.append(ent.text)
        return keywords

    def generate_prompt_from_keywords(self, keywords: List[str]) -> str:
        keyword_string = " ".join(keywords)
        prompt = self.generator(keyword_string, max_new_tokens=20, do_sample=True)
        return prompt[0]["generated_text"]

    def refine_prompts(self, prompts: List[str]) -> List[str]:
        """Refine the prompts using the BERT language model to score and rank them."""
        scores = []
        for prompt in prompts:
            input_ids = self.tokenizer.encode(prompt, add_special_tokens=True)
            input_ids = input_ids[:512]  # Truncate to max length for BERT
            with torch.no_grad():
                outputs = self.model(torch.tensor([input_ids]))
                predictions = outputs[0]
            loss = torch.nn.CrossEntropyLoss()
            score = loss(predictions.squeeze(), torch.tensor(input_ids)).item()
            scores.append((score, prompt))
        scores.sort(key=lambda x: x[0])  # Sort by score
        return [prompt for _, prompt in scores]

    def choose_best_prompt(self, prompts: List[str]) -> str:
        """Choose the best prompt from a list based on their BERT scores."""
        refined_prompts = self.refine_prompts(prompts)
        return refined_prompts[0]

    def generate_new_prompt_with_context(self, context: str) -> str:
        """Generate a new prompt based on a given context."""
        try:
            output = self.generator(context, max_new_tokens=20, do_sample=True)
            return output[0]["generated_text"]
        except Exception as e:
            logging.error(f"Error generating prompt with context: {str(e)}")
            return ""

    def _embed_text(self, text: str) -> List[float]:
        """
        Embed a piece of text as a list of floats using the specified transformer model.
        """
        embeddings = self.embedding_generator.encode([text])[0]
        return [float(i) for i in embeddings]

    def _embed_keywords(self, keywords: List[str]) -> List[List[float]]:
        """
        Embed a list of keywords as a list of embedded vectors using the specified transformer model.
        """
        embeddings = self.embedding_generator.encode(keywords)
        return [[float(i) for i in embedding] for embedding in embeddings]

    def compute_similar_keywords(
        self, keywords: List[str], num_keywords: int = 10
    ) -> List[str]:
        """
        Compute a list of similar keywords using the specified transformer model.
        """
        embeddings = self._embed_keywords(keywords)
        similar_keywords = []
        for i, (keyword, vector) in enumerate(zip(keywords, embeddings)):
            distances = []
            for j, embedding in enumerate(embeddings):
                if i != j:
                    distance = cosine(vector, embedding)
                    distances.append((distance, keywords[j]))
            distances.sort()
            similar_keywords.append(
                (keyword, [keyword for _, keyword in distances[:num_keywords]])
            )
        return similar_keywords
