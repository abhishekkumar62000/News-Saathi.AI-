import os
import math
import requests
import streamlit as st
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool  # type: ignore
from dotenv import load_dotenv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from newspaper import Article  # type: ignore
import nltk
nltk.download('punkt')

# Load environment variables
load_dotenv()

# Streamlit page config
st.set_page_config(
    page_title="News Saathi.AI",
    page_icon="🤖",
    layout="centered",
)

# Inject custom CSS for the hero section
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;800&display=swap');
    .hero {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #3F51B5 0%, #00ACC1 100%);
        color: white;
        padding: 2.5rem 1rem;
        margin: 2rem auto;
        max-width: 800px;
        border-radius: 1.5rem;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
        text-align: center;
    }
    .hero h1 {
        font-size: 3.5rem;
        margin: 0;
        line-height: 1.1;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
    }
    .hero p {
        font-size: 1.4rem;
        margin-top: 0.5rem;
        opacity: 0.9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the hero section
st.markdown(
    """
    <div class="hero">
      <h1>🤖 News Saathi.AI 🌐🔍</h1>
      <p>AI‑Driven Breaking News – With 🤖 News Saathi.AI 🌐</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Add Tabs for Content at the top
tab1, tab2, tab3, tab4 = st.tabs(["Generate Content", "Top 10 Indian Newspapers", "Trending News Analysis", "AI-Powered News Summarization"])

# Tab 1: Generate Content
with tab1:
    st.markdown("Generate comprehensive blog posts about any topic using AI agents.")

    # Sidebar
    with st.sidebar:
        st.header("Content Settings")
        
        # Make the text input take up more space
        topic = st.text_area(
            "Enter your topic",
            height=100,
            placeholder="Enter the topic you want to generate content about..."
        )
        
        # Add this in the sidebar
        suggested_topics = ["Artificial Intelligence", "Politics", "Climate Change", "Cryptocurrency", "Space Exploration", "Health and Wellness", "Technology AI Trends", "Cybersecurity", "Remote Work", "Digital Marketing"]
        selected_topic = st.selectbox("Or choose a suggested topic", ["None"] + suggested_topics)
        
        # Only use selected_topic if the user selects a specific topic
        if selected_topic != "None":
            topic = selected_topic
        
        # Add more sidebar controls if needed
        st.markdown("### Advanced Settings")
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
        
        # Add this in the sidebar
        theme = st.radio("Select Theme", ["Light", "Dark"], index=0)
        if theme == "Dark":
            st.markdown(
                """
                <style>
                body {
                    background-color: #2E2E2E;
                    color: white;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        
        # Add Tone Selector in the sidebar
        tone = st.selectbox(
            "Select Content Tone",
            ["Neutral", "Formal", "Informal", "Professional", "Conversational"],
            index=0
        )
        
        # Add Language Selector in the sidebar
        language = st.selectbox(
            "Select Language",
            ["English", "Hindi", "Maithili", "Bhojpuri", "Bangali", "Marathi"],
            index=0
        )
        
        # Add Summarization Option in the sidebar
        summarize = st.checkbox("Summarize Content", value=False)
        
        # Add some spacing
        st.markdown("---")
        
        # Make the generate button more prominent in the sidebar
        generate_button = st.button("Generate Content", type="primary", use_container_width=True)
        
        # Add some helpful information
        with st.expander("ℹ️ How to use"):
            st.markdown("""
            1. Enter your desired topic in the text area above
            2. Adjust the temperature if needed (higher = more creative)
            3. Click 'Generate Content' to start
            4. Wait for the AI to generate your article
            5. Download the result as a markdown file
            """)

        # Add the provided code snippet below "How to Use"
        image_path = "image.png"  # Ensure this file is in the same directory as your script
        try:
            st.sidebar.image(image_path)
        except FileNotFoundError:
            st.sidebar.warning("image.png file not found. Please check the file path.")
            
            
        AI_path = "AI.png"  # Ensure this file is in the same directory as your  script add top image
        try: 
           st.sidebar.image(AI_path)
        except FileNotFoundError:
            st.sidebar.warning("AI.png file not found. Please check the file path.")


        # Add Developer Information to Sidebar
        st.sidebar.markdown("👨👨‍💻Developer:- Abhishek❤️Yadav") 

        developer_path = "my.jpg"  # Ensure this file is in the same directory as your script
        try:
            st.sidebar.image(developer_path)
        except FileNotFoundError:
            st.sidebar.warning("my.jpg file not found. Please check the file path.")

def generate_content(topic, tone, language, summarize=False):
    llm = LLM(
        model="command-r",
        temperature=0.7
    )

    # Adjust the prompt to include the language and summarization
    prompt_language = f"Generate the content in {language} language."
    if summarize:
        prompt_language += " Summarize the content to make it concise and easy to read."

    search_tool = SerperDevTool(n_results=10)

    # First Agent: Senior Research Analyst
    senior_research_analyst = Agent(
        role="Senior Research Analyst",
        goal=f"Research, analyze, and synthesize comprehensive information on {topic} from reliable web sources. {prompt_language}",
        backstory="You're an expert research analyst with advanced web research skills. "
                "You excel at finding, analyzing, and synthesizing information from "
                "across the internet using search tools. You're skilled at "
                "distinguishing reliable sources from unreliable ones, "
                "fact-checking, cross-referencing information, and "
                "identifying key patterns and insights. You provide "
                "well-organized research briefs with proper citations "
                "and source verification. Your analysis includes both "
                "raw data and interpreted insights, making complex "
                "information accessible and actionable.",
        allow_delegation=False,
        verbose=True,
        tools=[search_tool],
        llm=llm
    )

    # Second Agent: Content Writer
    content_writer = Agent(
        role="Content Writer",
        goal=f"Transform research findings into engaging blog posts while maintaining accuracy. {prompt_language}",
        backstory="You're a skilled content writer specialized in creating "
                "engaging, accessible content from technical research. "
                "You work closely with the Senior Research Analyst and excel at maintaining the perfect "
                "balance between informative and entertaining writing, "
                "while ensuring all facts and citations from the research "
                "are properly incorporated. You have a talent for making "
                "complex topics approachable without oversimplifying them.",
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    # Research Task
    research_task = Task(
        description=("""Conduct comprehensive research on {topic} including:
            - Recent developments and news
            - Key industry trends and innovations
            - Expert opinions and analyses
            - Statistical data and market insights
            Evaluate source credibility and fact-check all information.
            Organize findings into a structured research brief.
            Include all relevant citations and sources.
        """),
        expected_output=f"""A detailed research report containing:
            - Executive summary of key findings
            - Comprehensive analysis of current trends and developments
            - List of verified facts and statistics
            - All citations and links to original sources
            - Clear categorization of main themes and patterns
            Please format with clear sections and bullet points for easy reference. {prompt_language}""",
        agent=senior_research_analyst
    )

    # Writing Task
    writing_task = Task(
        description=("""Using the research brief provided, create an engaging blog post that:
            1. Transforms technical information into accessible content
            2. Maintains all factual accuracy and citations from the research
            3. Includes:
                - Attention-grabbing introduction
                - Well-structured body sections with clear headings
                - Compelling conclusion, and Prediction 
            4. Preserves all source citations in [Source: URL] format
            5. Includes a 10 References section at the end
        """),
        expected_output=f"""A polished blog post in markdown format that:
            - Engages readers while maintaining accuracy
            - Contains properly structured sections
            - Includes Inline citations hyperlinked to the original source url
            - Presents information in an accessible yet informative way
            - Follows proper markdown formatting, use H1 for the title and H3 for the sub-sections. {prompt_language}""",
        agent=content_writer
    )

    # Create Crew
    crew = Crew(
        agents=[senior_research_analyst, content_writer],
        tasks=[research_task, writing_task],
        verbose=True
    )

    return crew.kickoff(inputs={"topic": topic, "tone": tone, "language": language, "summarize": summarize})

# Main content area
if generate_button:
    with st.spinner('Generating content... This may take a moment.'):
        try:
            result = generate_content(topic, tone=tone, language=language, summarize=summarize)
            st.markdown("### Generated Content")
            
            # Add collapsible preview
            with st.expander("🔍 Preview Content"):
                st.markdown(result)

            # Add download button
            st.download_button(
                label="Download Content",
                data=result.raw,
                file_name=f"{topic.lower().replace(' ', '_')}_article_{language.lower()}.md",
                mime="text/markdown"
            )
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # Add this after content generation
    st.markdown("### Suggested Images")
    unsplash_api_key = os.getenv("UNSPLASH_ACCESS_KEY")
    if unsplash_api_key:
        try:
            response = requests.get(
                f"https://api.unsplash.com/search/photos",
                params={"query": topic, "client_id": unsplash_api_key}
            )
            images = response.json().get("results", [])
            for img in images[:3]:  # Display top 3 images
                st.image(img["urls"]["small"], caption=img["alt_description"])
        except Exception as e:
            st.warning("Could not fetch images. Please check your API key.")
    else:
        st.warning("Unsplash API key is missing. Please set it in the .env file.")

# Add this before the Feedback section
st.markdown("### Summarize Content")
summarize = st.checkbox("Summarize the generated content", value=False)

# Feedback Section
st.markdown("### Feedback")
rating = st.slider("Rate the generated content", 1, 5, 3)
feedback = st.text_area("Any additional feedback?", placeholder="Let us know your thoughts...")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
    # Optionally, save feedback to a file or database

# Add Social Media Integration
st.markdown("### Share on Social Media")

# Define the content to share
share_message = f"Check out this amazing content generated by AI News Generator! 🚀"

# Twitter
twitter_url = f"https://twitter.com/intent/tweet?text={share_message}"
if st.button("Share on Twitter"):
    st.markdown(f"[Click here to share on Twitter]({twitter_url})", unsafe_allow_html=True)

# LinkedIn
linkedin_url = f"https://www.linkedin.com/sharing/share-offsite/?url=https://example.com"
if st.button("Share on LinkedIn"):
    st.markdown(f"[Click here to share on LinkedIn]({linkedin_url})", unsafe_allow_html=True)

# WhatsApp
whatsapp_url = f"https://api.whatsapp.com/send?text={share_message}"
if st.button("Share on WhatsApp"):
    st.markdown(f"[Click here to share on WhatsApp]({whatsapp_url})", unsafe_allow_html=True)

# Facebook
facebook_url = f"https://www.facebook.com/sharer/sharer.php?u=https://example.com"
if st.button("Share on Facebook"):
    st.markdown(f"[Click here to share on Facebook]({facebook_url})", unsafe_allow_html=True)

# Instagram (Instagram does not have a direct share URL for web apps)
if st.button("Share on Instagram"):
    st.warning("Instagram sharing is not supported directly. Please share manually.")

# Footer
st.markdown("---")
st.markdown("Built with CrewAI, Streamlit and powered by Cohere's Command R7B")

# Tab 2: Top 10 Indian Newspapers
with tab2:
    st.header("📰 Top 10 Indian Newspapers")
    st.markdown("Explore the top Indian newspapers. Click on the links below to visit their websites.")

    # List of top 10 Indian newspapers with their website links and logos
    newspapers = [
        {"name": "The Times of India", "url": "https://timesofindia.indiatimes.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/3/3e/Times_of_India_logo1.png"},
        {"name": "Hindustan Times", "url": "https://www.hindustantimes.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6c/Hindustan_Times_logo.png"},
        {"name": "The Hindu", "url": "https://www.thehindu.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/6/6d/The_Hindu_Logo.png"},
        {"name": "Indian Express", "url": "https://indianexpress.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/5/5e/The_Indian_Express_logo.png"},
        {"name": "Dainik Jagran", "url": "https://www.jagran.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Dainik_Jagran_logo.png"},
        {"name": "Amar Ujala", "url": "https://www.amarujala.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/3/3b/Amar_Ujala_logo.png"},
        {"name": "The Economic Times", "url": "https://economictimes.indiatimes.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/0c/The_Economic_Times_logo.png"},
        {"name": "Deccan Chronicle", "url": "https://www.deccanchronicle.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Deccan_Chronicle_logo.png"},
        {"name": "Navbharat Times", "url": "https://navbharattimes.indiatimes.com/", "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Navbharat_Times_logo.png"},
        {"name": "Punjab Kesari", "url": "https://www.punjabkesari.in/", "logo": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Punjab_Kesari_logo.png"}
    ]

    # Display each newspaper as a unique card with logo
    for newspaper in newspapers:
        st.markdown(
            f"""
            <div style="
                border: 2px solid #007BFF; 
                border-radius: 15px; 
                padding: 20px; 
                margin-bottom: 20px; 
                background: linear-gradient(135deg, #ffffff, #e6f7ff); 
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                text-align: center;
                display: flex;
                align-items: center;
                justify-content: space-between;
            ">
                <img src="{newspaper['logo']}" alt="{newspaper['name']} Logo" style="
                    width: 80px; 
                    height: auto; 
                    border-radius: 10px; 
                    margin-right: 20px;
                ">
                <div style="flex-grow: 1; text-align: left;">
                    <h2 style="margin: 0; color: #007BFF;">{newspaper['name']}</h2>
                    <a href="{newspaper['url']}" target="_blank" style="
                        display: inline-block; 
                        margin-top: 10px; 
                        padding: 10px 20px; 
                        color: white; 
                        background-color: #007BFF; 
                        text-decoration: none; 
                        border-radius: 5px;
                        font-weight: bold;
                    ">Visit Website</a>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Tab 3: Trending News Analysis
with tab3:
    st.header("📈 Trending News Analysis")
    st.markdown("Analyze trending news topics with sentiment analysis and keyword visualization.")

    # Fetch trending news using NewsAPI
    news_api_key = os.getenv("NEWS_API_KEY")
    if news_api_key:
        try:
            response = requests.get(
                "https://newsapi.org/v2/top-headlines",
                params={"country": "in", "apiKey": news_api_key}
            )
            # Check if the API request was successful
            if response.status_code == 200:
                articles = response.json().get("articles", [])
                
                if articles:
                    st.subheader("Trending Topics")
                    for article in articles[:5]:  # Display top 5 articles
                        st.markdown(f"**{article['title']}**")
                        st.markdown(f"*{article['description']}*")
                        st.markdown(f"[Read more]({article['url']})")
                    
                    # Perform sentiment analysis (dummy logic for now)
                    st.subheader("Sentiment Analysis")
                    sentiments = {"Positive": 0, "Neutral": 0, "Negative": 0}
                    for article in articles[:5]:
                        # Replace this with actual sentiment analysis logic
                        sentiment = "Neutral"  # Dummy sentiment
                        sentiments[sentiment] += 1
                    
                    st.bar_chart(sentiments)

                    # Generate a word cloud
                    st.subheader("Keyword Visualization")
                    all_titles = " ".join([article["title"] for article in articles])
                    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_titles)

                    fig, ax = plt.subplots()
                    ax.imshow(wordcloud, interpolation="bilinear")
                    ax.axis("off")
                    st.pyplot(fig)
                else:
                    st.warning("No trending news found. Try changing the country or query.")
            else:
                st.error(f"Failed to fetch news. API responded with status code {response.status_code}.")
                st.error(f"Response: {response.text}")
        except Exception as e:
            st.error(f"An error occurred while fetching news: {str(e)}")
    else:
        st.warning("NewsAPI key is missing. Please set it in the .env file.")

# Tab 4: AI-Powered News Summarization
with tab4:
    st.header("📰 AI-Powered News Summarization")
    st.markdown("Paste a news article URL or text below to generate a concise summary.")

    # Input options: URL or text
    input_type = st.radio("Input Type", ["URL", "Text"], index=0)

    if input_type == "URL":
        news_url = st.text_input("Enter the news article URL", placeholder="Paste the URL here...")
    else:
        news_text = st.text_area("Enter the news article text", placeholder="Paste the article text here...", height=200)

    # Summarization length options
    st.markdown("### Summarization Length")
    summary_length = st.radio("Choose the length of the summary", ["Short", "Medium", "Detailed"], index=1)

    # Generate summary button
    if st.button("Generate Summary"):
        with st.spinner("Generating summary..."):
            try:
                if input_type == "URL":
                    if not news_url:
                        st.error("Please provide a valid URL.")
                    else:
                        # Fetch the article content using newspaper3k
                        article = Article(news_url)
                        article.download()
                        article.parse()
                        article.nlp()  # Perform NLP for keywords and summary

                        # Use the article's summary
                        summary = article.summary
                        if not summary:
                            st.error("Could not generate a summary for the provided URL.")
                        else:
                            st.markdown("### Generated Summary")
                            st.write(summary)

                            # Add download button for the summary
                            st.download_button(
                                label="Download Summary",
                                data=summary,
                                file_name="news_summary.txt",
                                mime="text/plain"
                            )
                else:
                    if not news_text.strip():
                        st.error("Please provide the article text.")
                    else:
                        # Placeholder for text summarization logic
                        summary = f"Summary of the provided text ({summary_length} version)."
                        st.markdown("### Generated Summary")
                        st.write(summary)

                        # Add download button for the summary
                        st.download_button(
                            label="Download Summary",
                            data=summary,
                            file_name="news_summary.txt",
                            mime="text/plain"
                        )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
