Voice-Activated AI Assistant

A localized, modular voice assistant for macOS that integrates speech recognition, web automation, and local LLM capabilities via Ollama. This project allows you to control your browser, search shopping platforms, navigate via GPS, and interact with an AI through voice commands.

## 🚀 Features

-   **Voice Interaction**: Built-in speech-to-text (Google Speech Recognition) and text-to-speech (macOS `nsss` engine).
-   **Smart Web Search**: Quick searches for Google and YouTube.
-   **Shopping Integration**: Targeted searches on Amazon, Flipkart, Meesho, and Myntra.
-   **Entertainment Control**: Direct search/open functionality for Netflix, Prime Video, Hotstar, and Spotify.
-   **GPS Navigation**: Automated routing via Google Maps.
-   **Local AI Fallback**: Integrates with **Ollama (Llama 3)** to answer complex queries when no specific command is matched.

## 🛠️ Prerequisites

Before running the assistant, ensure you have the following installed:

1.  **Python 3.x**
2.  **Ollama**: [Download here](https://ollama.com/) and run `ollama run llama3` to pull the model.
3.  **Homebrew**: Required for some path configurations on macOS.
4.  **Dependencies**:
    ```bash
    pip install speechrecognition pyttsx3
    ```
    *Note: For macOS, `pyttsx3` uses the native `nsss` driver for better compatibility.*

## 📂 Project Structure

-   `index.py`: The main application script containing the logic for listening, command parsing, and executing actions.

## ⚙️ Setup & Usage

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Configure Environment**:
    The script automatically adds `/opt/homebrew/bin` to the system path to ensure `ollama` and other tools are accessible.

3.  **Run the Assistant**:
    ```bash
    python3 index.py
    ```

4.  **Voice Commands**:
    -   *General*: "Search [query]" or "YouTube [query]"
    -   *Shopping*: "Buy [product] on Amazon"
    -   *Navigation*: "Navigate to [destination]"
    -   *Entertainment*: "Play [song] on Spotify" or "Search [movie] on Netflix"
    -   *AI*: Ask any general question like "What is the capital of France?"
    -   *Exit*: Say "Stop", "Exit", "Quit", or "Bye".

## ⚠️ Known Issues / Notes

-   **Microphone Access**: Ensure your terminal or IDE has permission to access the microphone.
-   **Internet Connection**: Required for Google Speech Recognition and web navigation.
-   **Ollama**: The `ollama` service must be running in the background for AI responses to work.

## 📜 License

This project is open-source. Feel free to modify and distribute.
