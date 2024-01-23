# UB International Student Assistant Bot (RAG)

Welcome to the University at Buffalo (UB) International Student Assistant Bot repository! This chatbot leverages the power of Retrieval Augmented Generation (RAG) to provide precise and reliable information for international students at UB. By utilizing context documents from the official UB website, the bot ensures responses are up-to-date and rooted in the institution's verified content.

The bot operates on a backend powered by [Together.ai](https://together.ai/) API's Mistral 7B Large Language Model (LLM), with embeddings generated via the [OpenAI API](https://openai.com/api/), all orchestrated by the [\`llama-index\`](https://github.com/run-llama/llama_index) library. We have integrated this sophisticated tech stack into a user-friendly Streamlit web application hosted at [ub-iss.streamlit.app](https://ub-iss.streamlit.app), offering an intuitive interface for users to interact with.

## Features

- **Accurate Responses**: Utilizes verified University at Buffalo source material.
- **AI-Driven**: Powered by Mistral 7B LLM for natural language understanding.
- **State-of-the-Art Retrieval**: Embeddings created by the OpenAI API, ensuring high-quality informational retrieval.
- **User-Friendly Interface**: Provided through a Streamlit web application.

## Installation

Clone the repository with:

```sh
git clone https://github.com/billodalroy/ub-iss-chatbot.git
cd ub-iss-chatbot
```

Install the necessary libraries by running:

```sh
pip install -r requirements.txt
```

## Usage

To run the Streamlit web application locally, execute the following command from the root of the repository:

```sh
streamlit run app.py
```

Navigate to the local URL provided by Streamlit to interact with the chatbot.

## Deployment

The web application can be deployed to Streamlit sharing or any other suitable hosting platform capable of serving a Streamlit app. Ensure you configure the environmental variables for the Together.ai API and OpenAI API appropriately in your hosting environment.

## Contributing

We welcome contributions to the UB International Student Assistant Bot! If you have an idea for an improvement, please:

1. Fork the repository.
2. Create a new branch for your feature (\`git checkout -b feature/AmazingFeature\`).
3. Commit your changes (\`git commit -m 'Add some AmazingFeature'\`).
4. Push to the branch (\`git push origin feature/AmazingFeature\`).
5. Open a Pull Request.

## License

Distributed under the MIT License. See `LICENSE` for more information.
