"""Streamlit app for README-AI."""

import subprocess
import time
import os

import streamlit as st


def run_readmeai(api_key, output, repository):
    """Run the README-AI CLI."""
    if not output or not repository:
        st.error("Output path and repository path must be provided.")
        return

    command = [
        "readmeai",
        "-k",
        api_key,
        "-o",
        output,
        "-r",
        repository,
    ]

    st.session_state.generating = True

    with st.spinner("Generating README..."):
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            time.sleep(1)

            if result.returncode == 0:
                st.success("README-AI executed successfully!")
                try:
                    with open(output, "r", encoding="utf-8") as readme_file:
                        readme_content = readme_file.read()
                        st.subheader("Generated README.md:")
                        st.code(readme_content, language="markdown")
                        st.download_button(
                            "Download README.md",
                            data=readme_content,
                            file_name="README.md",
                        )
                except FileNotFoundError:
                    st.warning(
                        "README.md file not found. Please check the output path."
                    )
            else:
                st.error(f"Error running the README-AI: {result.stderr}")
        except subprocess.CalledProcessError as e:
            st.error(f"Error running the README-AI: {e}")
        finally:
            st.session_state.generating = False


def main():
    """Streamlit app entrypoint."""
    st.title("🤖 README-AI")
    st.write(
        "Provide your OpenAI API key, the output path and the repository path...and we'll do the rest! 🚀"
    )

    api_key = st.text_input("OpenAI API Key", type="password")
    os.environ["OPENAI_API_KEY"] = api_key
    output_path = st.text_input("Output File:")
    repository_path = st.text_input("Repository:")

    if st.button("Run"):
        run_readmeai(api_key, output_path, repository_path)
        if "generating" not in st.session_state or not st.session_state.generating:
            st.session_state.generating = False
            with st.empty():
                progress_bar = st.progress(0)
                for i in range(1, 101):
                    time.sleep(0.02)
                    progress_bar.progress(i)


if __name__ == "__main__":
    main()
