import gradio as gr
import os
from pathlib import Path
from loguru import logger

# Configure logging
logger.add("logs/app.log", rotation="500 MB")

def initialize_metagpt():
    """Initialize MetaGPT configuration"""
    metagpt_config = Path.home() / ".metagpt"
    metagpt_config.mkdir(exist_ok=True)
    logger.info(f"MetaGPT config initialized at {metagpt_config}")

def process_request(user_input: str, api_choice: str) -> str:
    """
    Process user requests using MetaGPT
    
    Args:
        user_input: User's request
        api_choice: Choice between OpenAI or Google Generative AI
    
    Returns:
        Response from the selected API
    """
    try:
        if not user_input.strip():
            return "❌ Please enter a valid request"
        
        if api_choice == "OpenAI":
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                return "❌ OpenAI API key not configured. Set OPENAI_API_KEY environment variable."
            
            logger.info(f"Processing with OpenAI: {user_input}")
            # Integration with OpenAI would go here
            return f"✅ OpenAI Response: Processing your request...\n\nInput: {user_input}"
        
        elif api_choice == "Google Generative AI":
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                return "❌ Google API key not configured. Set GOOGLE_API_KEY environment variable."
            
            logger.info(f"Processing with Google Generative AI: {user_input}")
            # Integration with Google Generative AI would go here
            return f"✅ Google Response: Processing your request...\n\nInput: {user_input}"
        
        else:
            return "❌ Invalid API choice"
    
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return f"❌ Error: {str(e)}"

def create_interface():
    """Create Gradio interface for MetaGPT"""
    
    with gr.Blocks(title="MetaGPT Web Interface") as interface:
        gr.Markdown("# 🤖 MetaGPT Web Interface")
        gr.Markdown("A powerful interface for MetaGPT - Multi-Agent Framework")
        
        with gr.Row():
            with gr.Column():
                user_input = gr.Textbox(
                    label="Your Request",
                    placeholder="Enter your request or task...",
                    lines=5,
                    interactive=True
                )
                
                api_choice = gr.Radio(
                    choices=["OpenAI", "Google Generative AI"],
                    label="Select AI Provider",
                    value="OpenAI"
                )
                
                submit_btn = gr.Button("🚀 Process Request", variant="primary")
            
            with gr.Column():
                output = gr.Textbox(
                    label="Response",
                    lines=10,
                    interactive=False
                )
        
        gr.Markdown("---")
        gr.Markdown("""
        ## ℹ️ Information
        - Ensure your API keys are set in environment variables
        - OPENAI_API_KEY for OpenAI
        - GOOGLE_API_KEY for Google Generative AI
        - Logs are stored in `logs/app.log`
        """)
        
        submit_btn.click(
            fn=process_request,
            inputs=[user_input, api_choice],
            outputs=output
        )
    
    return interface

if __name__ == "__main__":
    # Initialize
    initialize_metagpt()
    logger.info("Starting MetaGPT Web Interface...")
    
    # Create and launch interface
    interface = create_interface()
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )
