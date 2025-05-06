<!-- THIS IS ALL GENERATED DOCUMENTATION. DO NOT MODIFY THIS FILE -->
[asset-badge]: https://img.shields.io/badge/download%20asset-yes-blue.svg
[dense-reward-badge]: https://img.shields.io/badge/dense%20reward-yes-green.svg
[sparse-reward-badge]: https://img.shields.io/badge/sparse%20reward-yes-green.svg
[no-dense-reward-badge]: https://img.shields.io/badge/dense%20reward-no-red.svg
[no-sparse-reward-badge]: https://img.shields.io/badge/sparse%20reward-no-red.svg
[demos-badge]: https://img.shields.io/badge/demos-yes-green.svg
# COIN Primitive Tasks

Primitive task focus on the skill leaning of VLA, hopping to make the VLA be able to execute some basic skill.
## Primitive Tasks

The document here has both a high-level overview/list of all tasks in a table as well as detailed task cards with video demonstrations after.
| Name | Class | Scene Building | Reward Building | Dataset Collection | Initial State | Goal State | Instruction |
|------|-------|---------------|----------------|-------------------|--------------|-----------|-------------|
| <a href='#Tabletop-Close-Drawer'>Tabletop-Close-Drawer</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_v1_thumb_first.png' alt='Tabletop-Close-Drawer Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_v1_thumb_last.png' alt='Tabletop-Close-Drawer Goal'> | close the drawer |
| <a href='#Tabletop-Open-Drawer'>Tabletop-Open-Drawer</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Drawer_v1_thumb_first.png' alt='Tabletop-Open-Drawer Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Drawer_v1_thumb_last.png' alt='Tabletop-Open-Drawer Goal'> | open the drawer |
| <a href='#Tabletop-Close-Door'>Tabletop-Close-Door</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Door_v1_thumb_first.png' alt='Tabletop-Close-Door Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Door_v1_thumb_last.png' alt='Tabletop-Close-Door Goal'> | close the door |
| <a href='#Tabletop-Pull-Pivot'>Tabletop-Pull-Pivot</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pull_Pivot_v1_thumb_first.png' alt='Tabletop-Pull-Pivot Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pull_Pivot_v1_thumb_last.png' alt='Tabletop-Pull-Pivot Goal'> | pull the pivot to the target area |
| <a href='#Tabletop-Pick-Pen'>Tabletop-Pick-Pen</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Pen_v1_thumb_first.png' alt='Tabletop-Pick-Pen Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Pen_v1_thumb_last.png' alt='Tabletop-Pick-Pen Goal'> | pick up the pen and put it to the marker |
| <a href='#Tabletop-Put-Ball-IntoContainer'>Tabletop-Put-Ball-IntoContainer</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Ball_IntoContainer_v1_thumb_first.png' alt='Tabletop-Put-Ball-IntoContainer Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Ball_IntoContainer_v1_thumb_last.png' alt='Tabletop-Put-Ball-IntoContainer Goal'> | put the ball into the container  |
| <a href='#Tabletop-Open-Cabinet'>Tabletop-Open-Cabinet</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_v1_thumb_first.png' alt='Tabletop-Open-Cabinet Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_v1_thumb_last.png' alt='Tabletop-Open-Cabinet Goal'> | open the cabinet door |
| <a href='#Tabletop-Rotate-Holder'>Tabletop-Rotate-Holder</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Holder_v1_thumb_first.png' alt='Tabletop-Rotate-Holder Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Holder_v1_thumb_last.png' alt='Tabletop-Rotate-Holder Goal'> | rotate the holder till the hole upward |
| <a href='#Tabletop-Open-Trigger'>Tabletop-Open-Trigger</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Trigger_v1_thumb_first.png' alt='Tabletop-Open-Trigger Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Trigger_v1_thumb_last.png' alt='Tabletop-Open-Trigger Goal'> | turn on the trigger |
| <a href='#Tabletop-Rotate-Cube'>Tabletop-Rotate-Cube</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Cube_v1_thumb_first.png' alt='Tabletop-Rotate-Cube Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Cube_v1_thumb_last.png' alt='Tabletop-Rotate-Cube Goal'> | rotate the cube till the white face upward |
| <a href='#Tabletop-Close-Cabinet'>Tabletop-Close-Cabinet</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Cabinet_v1_thumb_first.png' alt='Tabletop-Close-Cabinet Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Cabinet_v1_thumb_last.png' alt='Tabletop-Close-Cabinet Goal'> | close the cabinet door |
| <a href='#Tabletop-Stack-Cubes'>Tabletop-Stack-Cubes</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Cubes_v1_thumb_first.png' alt='Tabletop-Stack-Cubes Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Cubes_v1_thumb_last.png' alt='Tabletop-Stack-Cubes Goal'> | stack all the cube |
| <a href='#Tabletop-Pick-Book-FromShelf'>Tabletop-Pick-Book-FromShelf</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Book_FromShelf_v1_thumb_first.png' alt='Tabletop-Pick-Book-FromShelf Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Book_FromShelf_v1_thumb_last.png' alt='Tabletop-Pick-Book-FromShelf Goal'> | Find and pick the book from the bookshelf and put it on the marker  |
| <a href='#Tabletop-Open-Microwave'>Tabletop-Open-Microwave</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Microwave_v1_thumb_first.png' alt='Tabletop-Open-Microwave Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Microwave_v1_thumb_last.png' alt='Tabletop-Open-Microwave Goal'> | open the microwave |
| <a href='#Tabletop-Close-Microwave'>Tabletop-Close-Microwave</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Microwave_v1_thumb_first.png' alt='Tabletop-Close-Microwave Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Microwave_v1_thumb_last.png' alt='Tabletop-Close-Microwave Goal'> | close the microwave |
| <a href='#Tabletop-Pick-Bottle'>Tabletop-Pick-Bottle</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Bottle_v1_thumb_first.png' alt='Tabletop-Pick-Bottle Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Bottle_v1_thumb_last.png' alt='Tabletop-Pick-Bottle Goal'> | pick up the bottle and put it on the marker |
| <a href='#Tabletop-Pick-Apple'>Tabletop-Pick-Apple</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Apple_v1_thumb_first.png' alt='Tabletop-Pick-Apple Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Apple_v1_thumb_last.png' alt='Tabletop-Pick-Apple Goal'> | pick the apple to the marker |
| <a href='#Tabletop-Open-Door'>Tabletop-Open-Door</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_v1_thumb_first.png' alt='Tabletop-Open-Door Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_v1_thumb_last.png' alt='Tabletop-Open-Door Goal'> | open the door  |
| <a href='#Tabletop-Pick-Cube-ToHolder'>Tabletop-Pick-Cube-ToHolder</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_ToHolder_v1_thumb_first.png' alt='Tabletop-Pick-Cube-ToHolder Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_ToHolder_v1_thumb_last.png' alt='Tabletop-Pick-Cube-ToHolder Goal'> | pick up the cube, put it in the holder |
| <a href='#Tabletop-Rotate-USB'>Tabletop-Rotate-USB</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_USB_v1_thumb_first.png' alt='Tabletop-Rotate-USB Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_USB_v1_thumb_last.png' alt='Tabletop-Rotate-USB Goal'> | Rotate the USB body for 90 degree with plug face left  |
| <a href='#Tabletop-Put-Fork-OnPlate'>Tabletop-Put-Fork-OnPlate</a> | Primitive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Fork_OnPlate_v1_thumb_first.png' alt='Tabletop-Put-Fork-OnPlate Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Fork_OnPlate_v1_thumb_last.png' alt='Tabletop-Put-Fork-OnPlate Goal'> | put the fork on the plate |

### Tabletop-Close-Drawer

**Environment ID:** `Tabletop-Close-Drawer-v1`

**Instruction:** close the drawer

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_v1_thumb_first.png' alt='Tabletop-Close-Drawer Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_v1_thumb_last.png' alt='Tabletop-Close-Drawer Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Open-Drawer

**Environment ID:** `Tabletop-Open-Drawer-v1`

**Instruction:** open the drawer

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Drawer_v1_thumb_first.png' alt='Tabletop-Open-Drawer Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Drawer_v1_thumb_last.png' alt='Tabletop-Open-Drawer Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Drawer_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Close-Door

**Environment ID:** `Tabletop-Close-Door-v1`

**Instruction:** close the door

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Door_v1_thumb_first.png' alt='Tabletop-Close-Door Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Door_v1_thumb_last.png' alt='Tabletop-Close-Door Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Door_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Pull-Pivot

**Environment ID:** `Tabletop-Pull-Pivot-v1`

**Instruction:** pull the pivot to the target area

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pull_Pivot_v1_thumb_first.png' alt='Tabletop-Pull-Pivot Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pull_Pivot_v1_thumb_last.png' alt='Tabletop-Pull-Pivot Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pull_Pivot_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Pick-Pen

**Environment ID:** `Tabletop-Pick-Pen-v1`

**Instruction:** pick up the pen and put it to the marker

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Pen_v1_thumb_first.png' alt='Tabletop-Pick-Pen Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Pen_v1_thumb_last.png' alt='Tabletop-Pick-Pen Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Pen_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Put-Ball-IntoContainer

**Environment ID:** `Tabletop-Put-Ball-IntoContainer-v1`

**Instruction:** put the ball into the container 

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Ball_IntoContainer_v1_thumb_first.png' alt='Tabletop-Put-Ball-IntoContainer Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Ball_IntoContainer_v1_thumb_last.png' alt='Tabletop-Put-Ball-IntoContainer Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Ball_IntoContainer_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Open-Cabinet

**Environment ID:** `Tabletop-Open-Cabinet-v1`

**Instruction:** open the cabinet door

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_v1_thumb_first.png' alt='Tabletop-Open-Cabinet Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_v1_thumb_last.png' alt='Tabletop-Open-Cabinet Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Rotate-Holder

**Environment ID:** `Tabletop-Rotate-Holder-v1`

**Instruction:** rotate the holder till the hole upward

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Holder_v1_thumb_first.png' alt='Tabletop-Rotate-Holder Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Holder_v1_thumb_last.png' alt='Tabletop-Rotate-Holder Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Holder_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Open-Trigger

**Environment ID:** `Tabletop-Open-Trigger-v1`

**Instruction:** turn on the trigger

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Trigger_v1_thumb_first.png' alt='Tabletop-Open-Trigger Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Trigger_v1_thumb_last.png' alt='Tabletop-Open-Trigger Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Trigger_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Rotate-Cube

**Environment ID:** `Tabletop-Rotate-Cube-v1`

**Instruction:** rotate the cube till the white face upward

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Cube_v1_thumb_first.png' alt='Tabletop-Rotate-Cube Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Cube_v1_thumb_last.png' alt='Tabletop-Rotate-Cube Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Cube_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Close-Cabinet

**Environment ID:** `Tabletop-Close-Cabinet-v1`

**Instruction:** close the cabinet door

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Cabinet_v1_thumb_first.png' alt='Tabletop-Close-Cabinet Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Cabinet_v1_thumb_last.png' alt='Tabletop-Close-Cabinet Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Cabinet_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Stack-Cubes

**Environment ID:** `Tabletop-Stack-Cubes-v1`

**Instruction:** stack all the cube

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Cubes_v1_thumb_first.png' alt='Tabletop-Stack-Cubes Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Cubes_v1_thumb_last.png' alt='Tabletop-Stack-Cubes Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Cubes_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Pick-Book-FromShelf

**Environment ID:** `Tabletop-Pick-Book-FromShelf-v1`

**Instruction:** Find and pick the book from the bookshelf and put it on the marker 

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Book_FromShelf_v1_thumb_first.png' alt='Tabletop-Pick-Book-FromShelf Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Book_FromShelf_v1_thumb_last.png' alt='Tabletop-Pick-Book-FromShelf Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Book_FromShelf_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Open-Microwave

**Environment ID:** `Tabletop-Open-Microwave-v1`

**Instruction:** open the microwave

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Microwave_v1_thumb_first.png' alt='Tabletop-Open-Microwave Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Microwave_v1_thumb_last.png' alt='Tabletop-Open-Microwave Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Microwave_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Close-Microwave

**Environment ID:** `Tabletop-Close-Microwave-v1`

**Instruction:** close the microwave

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Microwave_v1_thumb_first.png' alt='Tabletop-Close-Microwave Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Microwave_v1_thumb_last.png' alt='Tabletop-Close-Microwave Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Microwave_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Pick-Bottle

**Environment ID:** `Tabletop-Pick-Bottle-v1`

**Instruction:** pick up the bottle and put it on the marker

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Bottle_v1_thumb_first.png' alt='Tabletop-Pick-Bottle Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Bottle_v1_thumb_last.png' alt='Tabletop-Pick-Bottle Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Bottle_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Pick-Apple

**Environment ID:** `Tabletop-Pick-Apple-v1`

**Instruction:** pick the apple to the marker

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Apple_v1_thumb_first.png' alt='Tabletop-Pick-Apple Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Apple_v1_thumb_last.png' alt='Tabletop-Pick-Apple Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Apple_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Open-Door

**Environment ID:** `Tabletop-Open-Door-v1`

**Instruction:** open the door 

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_v1_thumb_first.png' alt='Tabletop-Open-Door Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_v1_thumb_last.png' alt='Tabletop-Open-Door Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Pick-Cube-ToHolder

**Environment ID:** `Tabletop-Pick-Cube-ToHolder-v1`

**Instruction:** pick up the cube, put it in the holder

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_ToHolder_v1_thumb_first.png' alt='Tabletop-Pick-Cube-ToHolder Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_ToHolder_v1_thumb_last.png' alt='Tabletop-Pick-Cube-ToHolder Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_ToHolder_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Rotate-USB

**Environment ID:** `Tabletop-Rotate-USB-v1`

**Instruction:** Rotate the USB body for 90 degree with plug face left 

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_USB_v1_thumb_first.png' alt='Tabletop-Rotate-USB Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_USB_v1_thumb_last.png' alt='Tabletop-Rotate-USB Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_USB_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Tabletop-Put-Fork-OnPlate

**Environment ID:** `Tabletop-Put-Fork-OnPlate-v1`

**Instruction:** put the fork on the plate

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Fork_OnPlate_v1_thumb_first.png' alt='Tabletop-Put-Fork-OnPlate Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Fork_OnPlate_v1_thumb_last.png' alt='Tabletop-Put-Fork-OnPlate Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Fork_OnPlate_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
