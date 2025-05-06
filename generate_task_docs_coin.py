# Code to generate task documentation automatically
TASK_CATEGORIES_TO_INCLUDE = [
    "coin_bench",
]

TASK_CATEGORIES_NAME_MAP = {"coin_bench": "coin_bench"}
GENERATED_TASKS_DOCS_FOLDER = "/home/lr-2002/project/reasoning_manipulation/ManiSkill/github_page/tasks"
GLOBAL_TASK_HEADER = """<!-- THIS IS ALL GENERATED DOCUMENTATION. DO NOT MODIFY THIS FILE -->
[asset-badge]: https://img.shields.io/badge/download%20asset-yes-blue.svg
[dense-reward-badge]: https://img.shields.io/badge/dense%20reward-yes-green.svg
[sparse-reward-badge]: https://img.shields.io/badge/sparse%20reward-yes-green.svg
[no-dense-reward-badge]: https://img.shields.io/badge/dense%20reward-no-red.svg
[no-sparse-reward-badge]: https://img.shields.io/badge/sparse%20reward-no-red.svg
[demos-badge]: https://img.shields.io/badge/demos-yes-green.svg
"""
GLOBAL_TASK_POST_HEADER = """
The document here has both a high-level overview/list of all tasks in a table as well as detailed task cards with video demonstrations after.
"""

TASK_CATEGORIES_HEADERS = {
    "coin_bench": """# COIN Bench Tasks

These are tasks from the COIN benchmark, split into Primitive and Interactive categories.""",
}

import gymnasium as gym 
import urllib.request
import mani_skill

from hmac import new
import gymnasium as gym
import numpy as np
import sapien.core as sapien
import os



from mani_skill.utils.download_demo import DATASET_SOURCES
from mani_skill.utils.registration import REGISTERED_ENVS
import os
import importlib
import inspect
from pathlib import Path


def generate_task_card(env, task_category):
    """Generate a markdown task card for an environment."""
    env_id = env.unwrapped.spec.id if hasattr(env.unwrapped, "spec") else env.spec.id
    task_name = env_id.split("-v")[0]
    task_version = env_id.split("-v")[1] if "-v" in env_id else "1"
    
    # Get task description and instruction
    doc = env.__doc__ or "No description available."
    instruction = getattr(env.unwrapped, "description", "No instruction provided.")
    
    # Format task name for URLs (replace hyphens with underscores)
    url_task_name = task_name.replace("-", "_") +'_v1'
    
    # Convert GitHub URLs to raw.githubusercontent.com for direct access
    image_url_first = f"https://github.com/Lr-2002/COIN_videos/blob/main/medias/{url_task_name}_thumb_first.png"
    image_url_first = image_url_first.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    
    image_url_last = f"https://github.com/Lr-2002/COIN_videos/blob/main/medias/{url_task_name}_thumb_last.png"
    image_url_last = image_url_last.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    
    video_url = f"https://github.com/Lr-2002/COIN_videos/blob/main/medias/{url_task_name}.mp4"
    video_url = video_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
    
    # Create markdown card
    card = f"""
### {task_name}

**Environment ID:** `{env_id}`

**Instruction:** {instruction}

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='{image_url_first}' alt='{task_name} Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='{image_url_last}' alt='{task_name} Goal State'>

**Video:**
<video width="400" controls>
  <source src="{video_url}" type="video/mp4">
  Your browser does not support the video tag.
</video>
"""
    return card


def main():
    base_dir = Path(__file__).parent / "source"

    # Get the path to mani_skill/envs/tasks
    tasks_dir = Path(mani_skill.envs.__file__).parent / "tasks"

    # Dictionary to store task info
    task_info = {}

    # Walk through all subfolders in tasks directory
    for root, dirs, files in os.walk(tasks_dir):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                # Get relative import path
                rel_path = os.path.relpath(os.path.join(root, file), tasks_dir.parent)
                module_path = rel_path.replace(os.sep, ".")[:-3]  # Remove .py

                # Import the module
                try:
                    module = importlib.import_module(f"mani_skill.envs.{module_path}")

                    # Find all classes defined in this module
                    classes = inspect.getmembers(module, inspect.isclass)

                    # Store classes that are defined in this module (not imported)
                    local_classes = [
                        cls
                        for name, cls in classes
                        if cls.__module__ == f"mani_skill.envs.{module_path}"
                    ]

                    if local_classes:
                        task_info[module_path] = local_classes

                except Exception as e:
                    print(f"Error importing {module_path}: {e}")
    # Filter to only include registered environment classes
    filtered_task_info = {}
    for module_path, classes in task_info.items():
        registered_classes = []
        for cls in classes:
            # Check if this class is registered as an environment
            for env_id, env_spec in REGISTERED_ENVS.items():
                if env_spec.cls == cls:
                    registered_classes.append(dict(env_id=env_id, cls=cls))
                    break
        if registered_classes:
            filtered_task_info[module_path] = registered_classes

    task_info = filtered_task_info
    # Categorize tasks by their type
    categorized_tasks = {k: [] for k in TASK_CATEGORIES_TO_INCLUDE}

    for module_path in task_info.keys():
        parts = module_path.split(".")
        if parts[0] == "tasks":
            category = parts[1]
            if category in categorized_tasks:
                categorized_tasks[category].append(module_path)

    # Generate documentation for each category
    print("Generating task docs in absolute path:", os.path.abspath(GENERATED_TASKS_DOCS_FOLDER))
    print("Expected task categories:")
    for c in TASK_CATEGORIES_TO_INCLUDE:
        print(f" - {c}")

    for task_category in categorized_tasks.keys():
        primitive_envs = []
        interactive_envs = []
        env_ids = []
        for module_path in categorized_tasks[task_category]:
            for d in task_info[module_path]:
                env_ids.append(d["env_id"])
                if 'interactive' in module_path:
                    interactive_envs.append(d['env_id'])

                else: 
                    primitive_envs.append(d['env_id'])

        if not env_ids:
            continue


        

        # Generate Primitive Tasks page
        with open(f"{GENERATED_TASKS_DOCS_FOLDER}/{task_category}_primitive.md", "w") as f:
            f.write(GLOBAL_TASK_HEADER)
            if task_category in TASK_CATEGORIES_HEADERS:
                f.write(TASK_CATEGORIES_HEADERS[task_category])
            f.write(f"\n## Primitive Tasks\n")
            f.write(GLOBAL_TASK_POST_HEADER)

            # Write table header
            f.write("| Name | Class | Scene Building | Reward Building | Dataset Collection | Initial State | Goal State | Instruction |\n")
            f.write("|------|-------|---------------|----------------|-------------------|--------------|-----------|-------------|\n")
            built_envs = []
            for env_id in primitive_envs:
                env = gym.make(
                    env_id,
                    obs_mode="rgb+depth+segmentation",  # Use rgbd to get camera observations
                    control_mode="pd_ee_delta_pose",
                    robot_uids="panda_wristcam",
                    render_mode="human",
                )
                built_envs.append(env)
                # env_id = env.unwrapped.spec.id if hasattr(env.unwrapped, "spec") else env.spec.id
                task_name = env_id.split("-v")[0]
                # Format task name for URLs (replace hyphens with underscores)
                url_task_name = task_name.replace("-", "_") + "_v1"
                
                # Convert GitHub URLs to raw.githubusercontent.com for direct access
                image_url_first = f"https://github.com/Lr-2002/COIN_videos/blob/main/medias/{url_task_name}_thumb_first.png"
                image_url_first = image_url_first.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                
                image_url_last = f"https://github.com/Lr-2002/COIN_videos/blob/main/medias/{url_task_name}_thumb_last.png"
                image_url_last = image_url_last.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                
                initial_image_html = f"<img style='width:100%;height:auto' src='{image_url_first}' alt='{task_name} Initial'>"
                goal_image_html = f"<img style='width:100%;height:auto' src='{image_url_last}' alt='{task_name} Goal'>"
                
                # Get instruction from env.description
                instruction = getattr(env.unwrapped, "description", "Perform the task successfully.")
                
                # Create a link to the task card with an anchor
                task_link = f"<a href='#{task_name.replace(' ', '-')}'>{task_name}</a>"
                
                f.write(
                    f"| {task_link} | Primitive | ✓ | ✓ | ✓ | {initial_image_html} | {goal_image_html} | {instruction} |\n"
                )

            # Detailed task cards for primitive tasks
            for env in built_envs:

                f.write(generate_task_card(env, task_category))
        # Generate Interactive Tasks page
        with open(f"{GENERATED_TASKS_DOCS_FOLDER}/{task_category}_interactive.md", "w") as f:
            f.write(GLOBAL_TASK_HEADER)
            if task_category in TASK_CATEGORIES_HEADERS:
                f.write(TASK_CATEGORIES_HEADERS[task_category])
            f.write(f"\n## Interactive Tasks\n")
            f.write(GLOBAL_TASK_POST_HEADER)

            # Write table header
            f.write("| Name | Class | Scene Building | Reward Building | Dataset Collection | Initial State | Goal State | Instruction | Query Image |\n")
            f.write("|------|-------|---------------|----------------|-------------------|--------------|-----------|-------------|-------------|\n")
            built_envs = []
            for env_id in interactive_envs:
                env = gym.make(
                    env_id,
                    obs_mode="rgb+depth+segmentation",  # Use rgbd to get camera observations
                    control_mode="pd_ee_delta_pose",
                    robot_uids="panda_wristcam",
                    render_mode="human",
                )
                built_envs.append(env)
                task_name = env_id.split("-v")[0]
                env.reset()
                query_text = getattr(env.unwrapped, "query_query", "Not available")
                query_image = getattr(env.unwrapped, "query_image", None)
                query_selection = getattr(env.unwrapped, "query_selection", {})
                query_answer = getattr(env.unwrapped, "query_answer", "Not available")
                # Format task name for URLs (replace hyphens with underscores)
                url_task_name = task_name.replace("-", "_") +'_v1'
                
                # Convert GitHub URLs to raw.githubusercontent.com for direct access
                image_url_first = f"https://github.com/Lr-2002/COIN_videos/blob/main/medias/{url_task_name}_thumb_first.png"
                image_url_first = image_url_first.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                
                image_url_last = f"https://github.com/Lr-2002/COIN_videos/blob/main/medias/{url_task_name}_thumb_last.png"
                image_url_last = image_url_last.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                
                initial_image_html = f"<img style='width:100%;height:auto' src='{image_url_first}' alt='{task_name} Initial'>"
                goal_image_html = f"<img style='width:100%;height:auto' src='{image_url_last}' alt='{task_name} Goal'>"
                
                query_image_cell = "-"
                if query_image is None:
                    query_image_url = f"https://github.com/Lr-2002/COIN_videos/blob/main/interactive_task_image/{url_task_name}.png"
                    query_image_url = query_image_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                    query_image_cell = f"<img style='width:100%;height:auto' src='{query_image_url}' alt='{task_name} Query'>"
                
                # Get instruction from env.description
                instruction = getattr(env.unwrapped, "description", "Perform the task successfully according to the query.")
                
                # Format query options for better display
                query_selection_text = ""
                if query_selection:
                    query_selection_text = "<div style='display:flex;flex-direction:column;gap:5px;'>"
                    for key, value in query_selection.items():
                        query_selection_text += f"<div><strong>{key}:</strong> {value}</div>"
                    query_selection_text += "</div>"
                    
                query_text_display = f"{query_text}<br><strong>Options:</strong>{query_selection_text}<br><strong>Answer:</strong> {query_answer}" if query_selection else query_text
                
                # Create a link to the task card with an anchor
                task_link = f"<a href='#{task_name.replace(' ', '-')}'>{task_name}</a>"
                
                f.write(
                    f"| {task_link} | Interactive | ✓ | ✓ | ✓ | {initial_image_html} | {goal_image_html} | {instruction} | {query_image_cell} |\n"
                )

            # Detailed task cards for interactive tasks with query_text and query_image
            for env in built_envs:
                # Initialize environment to get query information
                env.reset()
                env_id = env.unwrapped.spec.id if hasattr(env.unwrapped, "spec") else env.spec.id
                task_name = env_id.split("-v")[0]
                query_text = getattr(env.unwrapped, "query_query", "Not available")
                query_image = getattr(env.unwrapped, "query_image", None)
                query_selection = getattr(env.unwrapped, "query_selection", {})
                query_answer = getattr(env.unwrapped, "query_answer", "Not available")
                # Format task name for URLs (replace hyphens with underscores)
                url_task_name = task_name.replace("-", "_")
                
                query_image_info = ""
                if query_image is None:
                    query_image_url = f"https://github.com/Lr-2002/COIN_videos/blob/main/interactive_task_image/{url_task_name}.png"
                    query_image_url = query_image_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                    query_image_info = f"\n**Query Image:** <img style='max-width:300px;height:auto' src='{query_image_url}' alt='{task_name} Query'>"
                # Format options in a single column for markdown
                query_selection_text = ""
                if query_selection:
                    for key, value in query_selection.items():
                        query_selection_text += f"\n{key}: {value}"
                query_info = f"\n**Query Text:** {query_text}\n\n**Options:**{query_selection_text}\n\n**Answer:** {query_answer}{query_image_info}" if query_selection else f"\n**Query Text:** {query_text}{query_image_info}"
                card = generate_task_card(env, task_category)
                card += query_info + "\n"
                f.write(card)

    print(f"Generated task docs in {os.path.abspath(GENERATED_TASKS_DOCS_FOLDER)}")


if __name__ == "__main__":
    main()
