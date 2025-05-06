import streamlit as st
import json
import pandas as pd
import re
import html
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="COIN Benchmark", layout="wide", initial_sidebar_state="collapsed"
)

# -- Color palette from https://colorhunt.co/palette/bf92646f826abbd8a3f0f1c5
PRIMARY = "#BF9264"  # Warm brown
SECONDARY = "#6F826A"  # Forest green
BG1 = "#BBD8A3"  # Light green
BG2 = "#F0F1C5"  # Pale yellow

# Custom CSS - Simplified for better readability and reduced white space
st.markdown(
    f"""
    <style>
        body {{font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}}
        .stApp {{background-color: {BG2};}}
        .main {{background-color: {BG2}; padding: 1rem;}}
        h1, h2, h3, h4, h5, h6 {{font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}}
        
        /* Header styles - reduced padding */
        .main-header {{text-align: center; padding: 1.5rem 0; background-color: {PRIMARY}; border-radius: 8px; margin-bottom: 1.5rem; box-shadow: 0 2px 10px rgba(0,0,0,0.1);}}
        .main-header h1 {{color: white; font-size: 2.5rem; margin-bottom: 0.3rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);}}
        .main-header p {{color: white; font-size: 1.1rem; opacity: 0.9;}}
        
        /* Section styles - with BBD8A3 background for titles */
        .section {{background-color: {BG1}; padding: 1.5rem; border-radius: 8px; margin-bottom: 1.5rem; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}}
        .section-title {{color: #333333; font-size: 1.6rem; background-color: {BG1}; padding: 0.8rem 1.2rem; border-radius: 6px; margin-bottom: 1rem; box-shadow: 0 2px 4px rgba(0,0,0,0.0);}}
        
        /* Task card styles - with colored header and no white backgrounds */
        .task-card {{background-color: {BG2}; padding: 1.2rem; margin-bottom: 1.5rem; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.08);}}
        .task-card h3 {{color: white; margin-top: -1.2rem; margin-left: -1.2rem; margin-right: -1.2rem; margin-bottom: 1.2rem; font-size: 1.3rem; font-weight: 600; background-color: {PRIMARY}; padding: 0.8rem 1.2rem; border-radius: 8px 8px 0 0;}}
        .task-card p {{margin-bottom: 0.8rem; font-size: 0.95rem;}}
        .task-card pre {{background-color: rgba(0, 0, 0, 0.2); padding: 10px; border-radius: 5px; overflow-x: auto; font-family: monospace; font-size: 0.9rem; color: #f8f8f8;}}
        .task-card code {{font-family: monospace; background-color: rgba(0, 0, 0, 0.1); padding: 2px 4px; border-radius: 3px;}}
        .task-card .metadata {{display: flex; gap: 8px; margin-bottom: 0.8rem; flex-wrap: wrap; background-color: rgba(255, 255, 255, 0.2); padding: 0.8rem; border-radius: 6px;}}
        .task-card .metadata span {{background-color: {BG1}; color: {SECONDARY}; padding: 0.2rem 0.5rem; border-radius: 15px; font-size: 0.75rem; font-weight: 500;}}
        
        /* Interactive task styles - with matching design */
        .query-box {{background-color: rgba(255, 255, 255, 0.2); padding: 0.8rem; border-radius: 6px; margin: 15px 0;}}
        .query-box h4 {{margin-top: 0; color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px; margin-bottom: 10px; font-size: 1.1rem;}}
        .option {{background-color: rgba(255, 255, 255, 0.3); padding: 0.4rem 0.8rem; margin: 0.2rem 0; border-radius: 3px; font-size: 0.9rem;}}
        .answer {{font-weight: bold; color: {SECONDARY}; margin-top: 0.8rem; background-color: rgba(255, 255, 255, 0.3); padding: 0.4rem 0.8rem; border-radius: 3px;}}
        
        /* Table styles - matching the overall design */
        table {{width: 100%; border-collapse: collapse; margin: 0.8rem 0; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}}
        th {{background-color: {PRIMARY}; color: white; text-align: left; padding: 0.8rem; font-size: 0.9rem; font-weight: 600;}}
        td {{padding: 0.8rem; border-bottom: 1px solid rgba(255, 255, 255, 0.2); font-size: 0.9rem;}}
        tr:nth-child(even) {{background-color: rgba(255, 255, 255, 0.1);}}
        tr:nth-child(odd) {{background-color: rgba(255, 255, 255, 0.05);}}
        tr:hover {{background-color: rgba(255, 255, 255, 0.2); transition: background-color 0.2s ease;}}
        
        /* Media styles */
        img {{max-width: 100%; border-radius: 5px;}}
        video {{width: 100%; border-radius: 5px;}}
        
        /* Footer styles */
        .footer {{text-align: center; padding: 1rem; color: #666;}}
        .footer a {{color: {PRIMARY}; text-decoration: none; font-weight: 500;}}
        .footer a:hover {{text-decoration: underline;}}
        
        /* Make expander headers more outstanding */
        div.streamlit-expanderHeader {{background-color: {SECONDARY} !important; color: white !important; padding: 12px 18px !important; border-radius: 10px 10px 0 0 !important; margin-bottom: 0 !important; font-size: 1.6rem !important; font-weight: 700 !important; box-shadow: 0 3px 6px rgba(0,0,0,0.1) !important;}}
        div.streamlit-expanderHeader p {{color: white !important; font-weight: 700 !important; font-size: 1.6rem !important; text-shadow: 1px 1px 2px rgba(0,0,0,0.2) !important;}}
        div.streamlit-expanderContent {{border: 2px solid {SECONDARY} !important; border-top: none !important; border-radius: 0 0 10px 10px !important; padding: 18px !important; background-color: {BG2} !important;}}
        
        /* Make expander arrow white */
        button[kind="expanderHeaderButton"] svg {{fill: white !important;}}
        
        /* Fix markdown rendering */
        .task-content img {{max-width: 300px; height: auto;}}
        .task-content video {{max-width: 100%; height: auto;}}
        
        /* Streamlit component spacing fixes */
        .stTabs [data-baseweb="tab-list"] {{background-color: {BG1}; border-radius: 8px 8px 0 0; padding: 0.5rem 0.5rem 0 0.5rem;}}
        .stTabs [data-baseweb="tab"] {{font-size: 0.9rem; padding: 0.5rem 1rem;}}
        .stTabs [aria-selected="true"] {{background-color: {BG1}; color: {SECONDARY}; font-weight: bold;}}
        
        /* Reduce white space in columns */
        .row-widget.stButton {{margin-bottom: 0.5rem;}}
        .row-widget.stSelectbox {{margin-bottom: 0.5rem;}}
        div[data-testid="stVerticalBlock"] > div {{padding-top: 0.3rem; padding-bottom: 0.3rem;}}
        
        /* Task image container */
        .task-image-container {{display: flex; justify-content: space-between; margin-bottom: 15px;}}
        .task-image-container img {{max-width: 48%; height: auto;}}
        
        /* View details button */
        .view-details-btn {{
            background-color: {SECONDARY}; 
            color: white; 
            padding: 5px 10px; 
            border-radius: 5px; 
            text-decoration: none;
            display: inline-block;
            margin-top: 5px;
            font-size: 0.8rem;
        }}
        .view-details-btn:hover {{
            background-color: {PRIMARY};
        }}
    </style>
""",
    unsafe_allow_html=True,
)

# --- Header Section ---
st.markdown(
    """
    <div class="main-header">
        <h1>COIN Benchmark</h1>
        <p>Compositional Interaction for Robot Learning</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Introduction Section ---
st.markdown(
    """
    <div class="section">
        <h2 class="section-title">🎥 Introduction</h2>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    The COIN Benchmark (Compositional Interaction) is designed to evaluate and advance robot learning 
    for manipulation tasks. It features a diverse set of tasks ranging from simple primitive actions 
    to complex interactive scenarios requiring reasoning and planning.
    
    **Key features of COIN Benchmark:**
    - Realistic physics-based simulation environment
    - Diverse set of manipulation tasks with varying complexity
    - Support for both primitive and interactive task scenarios
    - Standardized evaluation metrics for fair comparison
    """)

with col2:
    # Introduction video
    video_path = Path("static/intro_video.mp4")
    if video_path.exists():
        st.video(str(video_path))
    else:
        st.image(
            "https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Balance_Pivot_WithBalls_v1_thumb_first.png",
            # "https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Balance_Pivot_WithBalls_v1.png",
            caption="COIN Benchmark Sample Task",
        )

st.markdown("</div>", unsafe_allow_html=True)

# --- Method Comparison ---
st.markdown(
    """
    <div class="section">
        <h2 class="section-title">📊 Method Comparison</h2>
    """,
    unsafe_allow_html=True,
)

# Create a DataFrame for better styling
comparison_data = pd.DataFrame(
    {
        "Method": ["GPT-4", "VoxPoser", "ReAct", "COIN-Teacher"],
        "Success Rate": ["87%", "75%", "66%", "90%"],
        "Generalization": ["High", "Medium", "Low", "High"],
        "Efficiency": ["Fast", "Moderate", "Slow", "Fast"],
        "Planning Ability": ["Excellent", "Good", "Fair", "Excellent"],
        "Adaptability": ["High", "Medium", "Low", "Very High"],
    }
)

st.table(comparison_data)
st.markdown("</div>", unsafe_allow_html=True)

# --- Task Overview ---
st.markdown(
    """
    <div class="section">
        <h2 class="section-title">🧩 Task Overview</h2>
    """,
    unsafe_allow_html=True,
)

task_tabs = st.tabs(["Primitive Tasks", "Interactive Tasks"])

# --- Primitive Tasks Tab ---
with task_tabs[0]:
    primitive_md_path = Path("tasks/coin_bench_primitive.md")

    if primitive_md_path.exists():
        primitive_md = primitive_md_path.read_text()

        # Extract task cards from markdown
        task_sections = re.split(r"\n### ", primitive_md)
        if task_sections:
            # Process header section separately
            header = task_sections[0]
            st.markdown(header, unsafe_allow_html=True)

            # Process each task card
            for i, section in enumerate(task_sections[1:], 1):
                section = (
                    "### " + section
                )  # Add back the heading that was removed in the split

                # Extract task name from the heading
                task_name_match = re.search(r"### ([^\n]+)", section)
                task_name = task_name_match.group(1) if task_name_match else f"Task {i}"

                # Extract description
                description_match = re.search(r"\*\*Description:\*\* ([^\n]+)", section)
                description = (
                    description_match.group(1)
                    if description_match
                    else "No description available."
                )

                # Extract environment ID
                env_id_match = re.search(r"\*\*Environment ID:\*\* `([^`]+)`", section)
                env_id = env_id_match.group(1) if env_id_match else ""

                # Extract instruction
                instruction_match = re.search(r"\*\*Instruction:\*\* ([^\n]+)", section)
                instruction = (
                    instruction_match.group(1)
                    if instruction_match
                    else "No instruction provided."
                )

                # Find all image URLs in the section
                image_urls = re.findall(r'src=[\'"]([^\'"]+)[\'"]', section)

                # Filter out video URLs (they contain .mp4)
                image_urls = [url for url in image_urls if not url.endswith(".mp4")]

                # Extract video URL
                video_match = re.search(r'<source src="([^"]+)"', section)
                video_url = video_match.group(1) if video_match else ""

                # Create image HTML if we have images
                image_html = ""
                if len(image_urls) >= 2:
                    image_html = f"""
                    <div style="margin: 15px 0;">
                        <h4 style="color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px; margin-bottom: 10px;">Task Images</h4>
                        <div style="display: flex; justify-content: space-between; gap: 20px; background-color: rgba(255, 255, 255, 0.2); padding: 15px; border-radius: 8px;">
                            <div style="text-align: center; width: 48%;">
                                <img src="{image_urls[0]}" style="width: 100%; object-fit: contain; border-radius: 6px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                                <p style="margin-top: 8px; font-weight: 500; color: {SECONDARY}; background-color: rgba(255, 255, 255, 0.3); padding: 5px; border-radius: 4px;">Initial State</p>
                            </div>
                            <div style="text-align: center; width: 48%;">
                                <img src="{image_urls[1]}" style="width: 100%; object-fit: contain; border-radius: 6px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                                <p style="margin-top: 8px; font-weight: 500; color: {SECONDARY}; background-color: rgba(255, 255, 255, 0.3); padding: 5px; border-radius: 4px;">Goal State</p>
                            </div>
                        </div>
                    </div>
                    """
                elif len(image_urls) == 1:
                    image_html = f"""
                    <div style="margin: 15px 0;">
                        <h4 style="color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px; margin-bottom: 10px;">Task Preview</h4>
                        <div style="text-align: center; background-color: rgba(255, 255, 255, 0.2); padding: 15px; border-radius: 8px;">
                            <img src="{image_urls[0]}" style="max-width: 80%; object-fit: contain; border-radius: 6px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                        </div>
                    </div>
                    """

                # Create video HTML if we have a video
                video_html = ""
                if video_url:
                    video_html = f"""
                    <div style="margin: 15px 0;">
                        <h4 style="color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px; margin-bottom: 10px;">Task Demonstration</h4>
                        <div style="background-color: rgba(255, 255, 255, 0.2); padding: 15px; border-radius: 8px;">
                            <div style="width:100%; margin-bottom:10px; border-radius: 6px; overflow: hidden; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                                <video width="100%" controls autoplay muted>
                                    <source src="{video_url}" type="video/mp4">
                                    Your browser does not support the video tag.
                                </video>
                            </div>
                            <p style="font-size:12px; color:#666; margin: 10px 0 0 0; text-align: center;">
                                If video doesn't appear, <a href="{video_url}" target="_blank" style="color: {PRIMARY}; font-weight: 500;">click here to open in new tab</a>
                            </p>
                        </div>
                    </div>
                    """

                # Create a task card using Streamlit's native components
                with st.container():
                    st.markdown(
                        f"<div id='{task_name.replace(' ', '-')}' class='task-card-anchor'></div>",
                        unsafe_allow_html=True,
                    )
                    with st.expander(f"**{task_name}**", expanded=False):
                        # st.markdown(f"**Description:** {description}")
                        st.markdown(f"**Environment ID:** `{env_id}`")
                        st.markdown(f"**Type:** Primitive")
                        st.markdown(f"**Instruction:** {instruction}")

                        # Display images
                        if len(image_urls) >= 2:
                            st.markdown(
                                f"<h4 style='color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px;'>Task Images</h4>",
                                unsafe_allow_html=True,
                            )
                            # Create a single row for all images
                            image_captions = ["Initial State", "Goal State"]
                            if len(image_urls) > 2:
                                image_captions.extend([f"View {i+1}" for i in range(2, len(image_urls))])
                            
                            # Display all images in a single row
                            st.image(
                                image_urls[:min(len(image_urls), 4)],  # Limit to 4 images to avoid overcrowding
                                caption=image_captions[:min(len(image_urls), 4)],
                                width=150  # Fixed width for each image
                            )
                        elif len(image_urls) == 1:
                            st.markdown(
                                f"<h4 style='color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px;'>Task Preview</h4>",
                                unsafe_allow_html=True,
                            )
                            st.image(
                                image_urls[0],
                                caption="Task Preview",
                                use_container_width=True,
                            )

                        # Display video
                        if video_url:
                            st.markdown(
                                f"<h4 style='color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px;'>Task Demonstration</h4>",
                                unsafe_allow_html=True,
                            )
                            st.video(video_url)
    else:
        st.warning("Primitive tasks documentation file not found.")

# --- Interactive Tasks Tab ---
with task_tabs[1]:
    # Add workflow lengths pie chart
    st.markdown(
        f"<h3 style='color: #333333; background-color: {BG1}; padding: 10px 15px; border-radius: 8px;'>Workflow Length Distribution</h3>",
        unsafe_allow_html=True,
    )
    
    # Read workflow lengths CSV
    workflow_csv_path = Path("static/workflow_lengths.csv")
    if workflow_csv_path.exists():
        import pandas as pd
        import plotly.graph_objects as go
        import plotly.express as px
        
        # Read the CSV file
        df = pd.read_csv(workflow_csv_path)
        
        # Create custom hover text
        hover_text = [f"{length} Steps: {count} tasks" for length, count in zip(df['flow_length'], df['number'])]
        
        # Create custom color scale based on BF9264 (warm brown)
        colors = [
            '#BF9264',  # Main warm brown
            '#D9B38C',  # Lighter warm brown
            '#A67C4E',  # Darker warm brown
            '#E6C9A8',  # Very light warm brown
            '#8C6B4A'   # Very dark warm brown
        ]
        
        # Create pie chart with Plotly
        fig = go.Figure(data=[go.Pie(
            labels=[f"{length} Steps" for length in df['flow_length']],
            values=df['number'],
            hoverinfo='label+percent+text',
            hovertext=hover_text,
            textinfo='percent',
            textfont=dict(size=14, color='#333333'),
            marker=dict(
                colors=colors,
                line=dict(color='#FFFFFF', width=1.5)
            ),
            pull=[0.05] * len(df)  # Slight pull for all slices
        )])
        
        # Update layout
        fig.update_layout(
            title={
                'text': "Distribution of Workflow Lengths",
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(size=20, color='#333333')
            },
            legend=dict(
                title="Workflow Lengths",
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5
            ),
            margin=dict(t=80, b=80, l=40, r=40),
            height=500,
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
            plot_bgcolor='rgba(0,0,0,0)',   # Transparent plot area
            font=dict(color='#333333')      # Default font color
        )
        
        # Display the chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)
        
        # Display total number of tasks
        total_tasks = df['number'].sum()
        st.info(f"Total number of tasks: {total_tasks}")
    else:
        st.warning("Workflow lengths CSV file not found.")
    
    # Add video frame count pie chart
    st.markdown(
        f"<h3 style='color: #333333; background-color: {BG1}; padding: 10px 15px; border-radius: 8px;'>Video Frame Count Distribution</h3>",
        unsafe_allow_html=True,
    )
    
    # Read video frames CSV
    video_frames_csv_path = Path("static/video_frames.csv")
    if video_frames_csv_path.exists():
        # Import required libraries if not already imported
        import pandas as pd
        import plotly.graph_objects as go
        import plotly.express as px
        
        # Read the CSV file
        df_frames = pd.read_csv(video_frames_csv_path)
        
        # Create custom hover text
        hover_text_frames = [f"{frame_range}: {count} videos" for frame_range, count in zip(df_frames['frame_range'], df_frames['number'])]
        
        # Create custom color scale for frames chart
        frame_colors = [
            '#BF9264',  # Main warm brown
            '#D9B38C',  # Lighter warm brown
            '#A67C4E',  # Darker warm brown
            '#E6C9A8'   # Very light warm brown
        ]
        
        # Create pie chart with Plotly
        fig_frames = go.Figure(data=[go.Pie(
            labels=[f"{frame_range}" for frame_range in df_frames['frame_range']],
            values=df_frames['number'],
            hoverinfo='label+percent+text',
            hovertext=hover_text_frames,
            textinfo='percent',
            textfont=dict(size=14, color='#333333'),
            marker=dict(
                colors=frame_colors,
                line=dict(color='#FFFFFF', width=1.5)
            ),
            pull=[0.05] * len(df_frames)  # Slight pull for all slices
        )])
        
        # Update layout
        fig_frames.update_layout(
            title={
                'text': "Distribution of Video Frame Counts",
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(size=20, color='#333333')
            },
            legend=dict(
                title="Frame Ranges",
                orientation="h",
                yanchor="bottom",
                y=-0.2,
                xanchor="center",
                x=0.5
            ),
            margin=dict(t=80, b=80, l=40, r=40),
            height=500,
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
            plot_bgcolor='rgba(0,0,0,0)',   # Transparent plot area
            font=dict(color='#333333')      # Default font color
        )
        
        # Display the chart in Streamlit
        st.plotly_chart(fig_frames, use_container_width=True)
        
        # Display total number of videos
        total_videos = df_frames['number'].sum()
        st.info(f"Total number of videos: {total_videos}")
    else:
        st.warning("Video frames CSV file not found.")
    
    # Add skill distribution histogram
    st.markdown(
        f"<h3 style='color: #333333; background-color: {BG1}; padding: 10px 15px; border-radius: 8px;'>Skill Distribution Across Tasks</h3>",
        unsafe_allow_html=True,
    )
    
    # Read skill distribution CSV
    skill_dist_csv_path = Path("static/skill_distribution.csv")
    if skill_dist_csv_path.exists():
        # Import required libraries if not already imported
        import pandas as pd
        import plotly.graph_objects as go
        import plotly.express as px
        
        # Read the CSV file
        df_skills = pd.read_csv(skill_dist_csv_path)
        
        # Sort by count in descending order
        df_skills = df_skills.sort_values('count', ascending=False)
        
        # Create a custom color gradient based on the count
        color_scale = [
            '#BF9264',  # Main warm brown
            '#D9B38C',  # Lighter warm brown
            '#A67C4E',  # Darker warm brown
            '#E6C9A8',  # Very light warm brown
            '#8C6B4A'   # Very dark warm brown
        ]
        
        # Create histogram with Plotly
        fig_skills = go.Figure(data=[go.Bar(
            x=df_skills['skill'],
            y=df_skills['count'],
            text=df_skills['count'],
            textposition='auto',
            hoverinfo='x+y',
            marker=dict(
                color=df_skills['count'],
                colorscale=color_scale,
                line=dict(color='#FFFFFF', width=1.5)
            )
        )])
        
        # Update layout
        fig_skills.update_layout(
            title={
                'text': "Distribution of Skills Across Tasks",
                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top',
                'font': dict(size=20, color='#333333')
            },
            xaxis=dict(
                title=dict(text="Skill", font=dict(size=16, color='#333333')),
                tickfont=dict(size=14, color='#333333')
            ),
            yaxis=dict(
                title=dict(text="Number of Tasks", font=dict(size=16, color='#333333')),
                tickfont=dict(size=14, color='#333333')
            ),
            margin=dict(t=80, b=80, l=40, r=40),
            height=500,
            paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
            plot_bgcolor='rgba(0,0,0,0)',   # Transparent plot area
            font=dict(color='#333333')      # Default font color
        )
        
        # Display the chart in Streamlit
        st.plotly_chart(fig_skills, use_container_width=True)
        
        # Display total number of skills
        total_skill_occurrences = df_skills['count'].sum()
        unique_skills = len(df_skills)
        st.info(f"Total of {unique_skills} unique skills across {total_skill_occurrences} skill occurrences in all tasks")
    else:
        st.warning("Skill distribution CSV file not found.")
    
    # Continue with interactive tasks documentation
    interactive_md_path = Path("tasks/coin_bench_interactive.md")
    
    if interactive_md_path.exists():
        interactive_md = interactive_md_path.read_text()

        # Extract task cards from markdown
        task_sections = re.split(r"\n### ", interactive_md)
        if task_sections:
            # Process header section separately
            header = task_sections[0]
            st.markdown(header, unsafe_allow_html=True)

            # Process each task card
            for i, section in enumerate(task_sections[1:], 1):
                section = (
                    "### " + section
                )  # Add back the heading that was removed in the split

                # Extract task name from the heading
                task_name_match = re.search(r"### ([^\n]+)", section)
                task_name = task_name_match.group(1) if task_name_match else f"Task {i}"

                # Extract description
                description_match = re.search(r"\*\*Description:\*\* ([^\n]+)", section)
                description = (
                    description_match.group(1)
                    if description_match
                    else "No description available."
                )

                # Extract environment ID
                env_id_match = re.search(r"\*\*Environment ID:\*\* `([^`]+)`", section)
                env_id = env_id_match.group(1) if env_id_match else ""

                # Extract instruction
                instruction_match = re.search(r"\*\*Instruction:\*\* ([^\n]+)", section)
                instruction = (
                    instruction_match.group(1)
                    if instruction_match
                    else "No instruction provided."
                )

                # Extract query text, options, and answer
                query_text_match = re.search(r"\*\*Query Text:\*\* ([^\n]+)", section)
                query_text = (
                    query_text_match.group(1)
                    if query_text_match
                    else "No query available."
                )

                # Extract options
                options_section = ""
                options_match = re.search(
                    r"\*\*Options:\*\*\n([^\n]+\n[^\n]+\n[^\n]+)", section
                )
                if options_match:
                    options_section = options_match.group(1)

                # Extract answer
                answer_match = re.search(r"\*\*Answer:\*\* ([^\n]+)", section)
                answer = answer_match.group(1) if answer_match else "Not available"

                # Initialize query_image_html to avoid unbound variable issues
                query_image_html = ""

                # Find all image URLs in the section
                image_urls = re.findall(r'src=[\'"]([^\'"]+)[\'"]', section)

                # Filter out video URLs (they contain .mp4)
                image_urls = [url for url in image_urls if not url.endswith(".mp4")]

                # Extract video URL
                video_match = re.search(r'<source src="([^"]+)"', section)
                video_url = video_match.group(1) if video_match else ""

                # Create image HTML if we have images
                image_html = ""
                if len(image_urls) >= 2:
                    image_html = f"""
                    <div style="margin: 15px 0;">
                        <h4 style="color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px; margin-bottom: 10px;">Task Images</h4>
                        <div style="display: flex; justify-content: space-between; gap: 20px; background-color: rgba(255, 255, 255, 0.2); padding: 15px; border-radius: 8px;">
                            <div style="text-align: center; width: 48%;">
                                <img src="{image_urls[0]}" style="width: 100%; object-fit: contain; border-radius: 6px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                                <p style="margin-top: 8px; font-weight: 500; color: {SECONDARY}; background-color: rgba(255, 255, 255, 0.3); padding: 5px; border-radius: 4px;">Initial State</p>
                            </div>
                            <div style="text-align: center; width: 48%;">
                                <img src="{image_urls[1]}" style="width: 100%; object-fit: contain; border-radius: 6px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                                <p style="margin-top: 8px; font-weight: 500; color: {SECONDARY}; background-color: rgba(255, 255, 255, 0.3); padding: 5px; border-radius: 4px;">Goal State</p>
                            </div>
                        </div>
                    </div>
                    """
                elif len(image_urls) == 1:
                    image_html = f"""
                    <div style="margin: 15px 0;">
                        <h4 style="color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px; margin-bottom: 10px;">Task Preview</h4>
                        <div style="text-align: center; background-color: rgba(255, 255, 255, 0.2); padding: 15px; border-radius: 8px;">
                            <img src="{image_urls[0]}" style="max-width: 80%; object-fit: contain; border-radius: 6px; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                        </div>
                    </div>
                    """

                # Create video HTML if we have a video
                video_html = ""
                if video_url:
                    video_html = f"""
                    <div style="margin: 15px 0;">
                        <h4 style="color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px; margin-bottom: 10px;">Task Demonstration</h4>
                        <div style="background-color: rgba(255, 255, 255, 0.2); padding: 15px; border-radius: 8px;">
                            <div style="width:100%; margin-bottom:10px; border-radius: 6px; overflow: hidden; box-shadow: 0 3px 6px rgba(0,0,0,0.1);">
                                <video width="100%" controls autoplay muted>
                                    <source src="{video_url}" type="video/mp4">
                                    Your browser does not support the video tag.
                                </video>
                            </div>
                            <p style="font-size:12px; color:#666; margin: 10px 0 0 0; text-align: center;">
                                If video doesn't appear, <a href="{video_url}" target="_blank" style="color: {PRIMARY}; font-weight: 500;">click here to open in new tab</a>
                            </p>
                        </div>
                    </div>
                    """

                # Create query HTML - escape HTML in query_text
                import html

                escaped_query_text = html.escape(query_text)
                query_html = f"""
                <div style="margin: 15px 0;">
                    <h4 style="color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px; margin-bottom: 10px;">Query Information</h4>
                    <div style="background-color: {BG2}; padding: 15px; border-radius: 8px;">
                        <p style="background-color: rgba(255, 255, 255, 0.3); padding: 10px; border-radius: 6px;"><strong>Query Text:</strong> {escaped_query_text}</p>
                    </div>
                </div>
                """

                # Create options HTML - escape HTML in options and answer
                options_html = ""
                if options_section:
                    options_list = ""
                    for option_line in options_section.split("\n"):
                        if option_line.strip():
                            escaped_option = html.escape(option_line.strip())
                            options_list += f'<div style="background-color: rgba(255, 255, 255, 0.3); padding: 0.4rem 0.8rem; margin: 0.4rem 0; border-radius: 4px;">{escaped_option}</div>'

                    escaped_answer = html.escape(answer)
                    options_html = f"""
                    <div style="margin: 15px 0;">
                        <h4 style="color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px; margin-bottom: 10px;">Options</h4>
                        <div style="background-color: {BG2}; padding: 15px; border-radius: 8px;">
                            {options_list}
                            <div style="background-color: rgba(255, 255, 255, 0.4); padding: 0.6rem 0.8rem; margin-top: 0.8rem; border-radius: 4px; font-weight: bold; color: {SECONDARY};"><strong>Answer:</strong> {escaped_answer}</div>
                        </div>
                    </div>
                    """

                # Extract query image URL
                query_image_match = re.search(
                    r"\*\*Query Image:\*\* !\[.*?\]\(([^)]+)\)", section
                )
                query_image_url = (
                    query_image_match.group(1) if query_image_match else ""
                )

                # Create a task card using Streamlit's native components
                with st.container():
                    st.markdown(
                        f"<div id='{task_name.replace(' ', '-')}' class='task-card-anchor'></div>",
                        unsafe_allow_html=True,
                    )
                    with st.expander(f"**{task_name}**", expanded=False):
                        # st.markdown(f"**Description:** {description}")
                        st.markdown(f"**Environment ID:** `{env_id}`")
                        st.markdown(f"**Type:** Interactive")
                        st.markdown(f"**Instruction:** {instruction}")

                        # Display images
                        if len(image_urls) >= 2:
                            st.markdown(
                                f"<h4 style='color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px;'>Task Images</h4>",
                                unsafe_allow_html=True,
                            )
                            # Create a single row for all images
                            image_captions = ["Initial State", "Goal State"]
                            if len(image_urls) > 2:
                                image_captions.extend([f"View {i+1}" for i in range(2, len(image_urls))])
                            
                            # Display all images in a single row
                            st.image(
                                image_urls[:min(len(image_urls), 4)],  # Limit to 4 images to avoid overcrowding
                                caption=image_captions[:min(len(image_urls), 4)],
                                width=150  # Fixed width for each image
                            )
                        elif len(image_urls) == 1:
                            st.markdown(
                                f"<h4 style='color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px;'>Task Preview</h4>",
                                unsafe_allow_html=True,
                            )
                            st.image(
                                image_urls[0],
                                caption="Task Preview",
                                use_container_width=True,
                            )

                        # Display video
                        if video_url:
                            st.markdown(
                                f"<h4 style='color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px;'>Task Demonstration</h4>",
                                unsafe_allow_html=True,
                            )
                            st.video(video_url)

                        # Display query information
                        st.markdown(
                            f"<h4 style='color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px;'>Query Information</h4>",
                            unsafe_allow_html=True,
                        )
                        st.markdown(f"**Query Text:** {query_text}")

                        # Display query image if available
                        if query_image_url:
                            st.image(
                                query_image_url,
                                caption="Query Image",
                                use_container_width=True,
                            )

                        # Display options and answer
                        if options_section:
                            st.markdown(
                                f"<h4 style='color: #333333; background-color: {BG1}; padding: 8px 12px; border-radius: 6px;'>Options</h4>",
                                unsafe_allow_html=True,
                            )
                            for option_line in options_section.split("\n"):
                                if option_line.strip():
                                    st.markdown(f"- {option_line.strip()}")

                            st.markdown(f"**Answer:** {answer}")

                # We're now using Streamlit's native components for displaying all content, so no additional HTML is needed
    else:
        st.warning("Interactive tasks documentation file not found.")

st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown(
    f"""
    <div class="section">
        <div class="footer">
            <p>© 2025 COIN Benchmark</p>
            <p>
                <a href="https://github.com/Lr-2002/COIN_videos" target="_blank">GitHub Repository</a> | 
                <a href="#">Research Paper</a> | 
                <a href="#">Documentation</a>
            </p>
            <p>Developed by the ML Group at BIGAI</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
