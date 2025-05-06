<!-- THIS IS ALL GENERATED DOCUMENTATION. DO NOT MODIFY THIS FILE -->

# COIN Interactive Tasks

Interactive task mainly focus on how to interactive and reason conditioned on the inteaction-context and make right decision.
There are still VQA Support for such tasks, please refer to the table for detail.

## Interactive Tasks

The document here has both a high-level overview/list of all tasks in a table as well as detailed task cards with video demonstrations after.

| Name | Class | Scene Building | Reward Building | Demo Collection | Initial State | Goal State | Instruction | Query Image |
|------|-------|---------------|----------------|-------------------|--------------|-----------|-------------|-------------|
| <a href='#Tabletop-Balance-Pivot-WithBalls'>Tabletop-Balance-Pivot-WithBalls</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Balance_Pivot_WithBalls_v1_thumb_first.png' alt='Tabletop-Balance-Pivot-WithBalls Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Balance_Pivot_WithBalls_v1_thumb_last.png' alt='Tabletop-Balance-Pivot-WithBalls Goal'> | Balance the long board on the triangular prism and place the cubes to maintain balance | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Balance_Pivot_WithBalls_v1.png' alt='Tabletop-Balance-Pivot-WithBalls Query'> |
| <a href='#Tabletop-Open-Door-WithObstacle'>Tabletop-Open-Door-WithObstacle</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_WithObstacle_v1_thumb_first.png' alt='Tabletop-Open-Door-WithObstacle Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_WithObstacle_v1_thumb_last.png' alt='Tabletop-Open-Door-WithObstacle Goal'> | open the door | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Open_Door_WithObstacle_v1.png' alt='Tabletop-Open-Door-WithObstacle Query'> |
| <a href='#Tabletop-Find-Dice'>Tabletop-Find-Dice</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Dice_v1_thumb_first.png' alt='Tabletop-Find-Dice Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Dice_v1_thumb_last.png' alt='Tabletop-Find-Dice Goal'> | find the dice which have 2 and 4 point in the corresponding face and put it on the marker | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Find_Dice_v1.png' alt='Tabletop-Find-Dice Query'> |
| <a href='#Tabletop-Seek-Holder-InCabinet'>Tabletop-Seek-Holder-InCabinet</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Holder_InCabinet_v1_thumb_first.png' alt='Tabletop-Seek-Holder-InCabinet Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Holder_InCabinet_v1_thumb_last.png' alt='Tabletop-Seek-Holder-InCabinet Goal'> | Find the holder containing an eraser the cabinet, put it to the marker | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Seek_Holder_InCabinet_v1.png' alt='Tabletop-Seek-Holder-InCabinet Query'> |
| <a href='#Tabletop-Stack-Cube-WithColor'>Tabletop-Stack-Cube-WithColor</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Cube_WithColor_v1_thumb_first.png' alt='Tabletop-Stack-Cube-WithColor Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Cube_WithColor_v1_thumb_last.png' alt='Tabletop-Stack-Cube-WithColor Goal'> | Stack the cube with same color | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Stack_Cube_WithColor_v1.png' alt='Tabletop-Stack-Cube-WithColor Query'> |
| <a href='#Tabletop-Stack-LongObjects'>Tabletop-Stack-LongObjects</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_LongObjects_v1_thumb_first.png' alt='Tabletop-Stack-LongObjects Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_LongObjects_v1_thumb_last.png' alt='Tabletop-Stack-LongObjects Goal'> | stack all the objects to make it most high | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Stack_LongObjects_v1.png' alt='Tabletop-Stack-LongObjects Query'> |
| <a href='#Tabletop-Put-Cube-IntoCabinetWithObstacle'>Tabletop-Put-Cube-IntoCabinetWithObstacle</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Cube_IntoCabinetWithObstacle_v1_thumb_first.png' alt='Tabletop-Put-Cube-IntoCabinetWithObstacle Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Cube_IntoCabinetWithObstacle_v1_thumb_last.png' alt='Tabletop-Put-Cube-IntoCabinetWithObstacle Goal'> |  put the object into the cabinet | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Put_Cube_IntoCabinetWithObstacle_v1.png' alt='Tabletop-Put-Cube-IntoCabinetWithObstacle Query'> |
| <a href='#Tabletop-Lift-Book'>Tabletop-Lift-Book</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Lift_Book_v1_thumb_first.png' alt='Tabletop-Lift-Book Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Lift_Book_v1_thumb_last.png' alt='Tabletop-Lift-Book Goal'> | lift the book up to the higher platform | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Lift_Book_v1.png' alt='Tabletop-Lift-Book Query'> |
| <a href='#Tabletop-Close-Cabinet-WithObstacle'>Tabletop-Close-Cabinet-WithObstacle</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Cabinet_WithObstacle_v1_thumb_first.png' alt='Tabletop-Close-Cabinet-WithObstacle Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Cabinet_WithObstacle_v1_thumb_last.png' alt='Tabletop-Close-Cabinet-WithObstacle Goal'> | open the cabinet door | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Close_Cabinet_WithObstacle_v1.png' alt='Tabletop-Close-Cabinet-WithObstacle Query'> |
| <a href='#Tabletop-Seek-Objects-WithObstacle'>Tabletop-Seek-Objects-WithObstacle</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Objects_WithObstacle_v1_thumb_first.png' alt='Tabletop-Seek-Objects-WithObstacle Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Objects_WithObstacle_v1_thumb_last.png' alt='Tabletop-Seek-Objects-WithObstacle Goal'> | find the cube in the cabinet and pick it up | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Seek_Objects_WithObstacle_v1.png' alt='Tabletop-Seek-Objects-WithObstacle Query'> |
| <a href='#Tabletop-Close-Drawer-WithLongObstacle'>Tabletop-Close-Drawer-WithLongObstacle</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_WithLongObstacle_v1_thumb_first.png' alt='Tabletop-Close-Drawer-WithLongObstacle Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_WithLongObstacle_v1_thumb_last.png' alt='Tabletop-Close-Drawer-WithLongObstacle Goal'> | close the drawer | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Close_Drawer_WithLongObstacle_v1.png' alt='Tabletop-Close-Drawer-WithLongObstacle Query'> |
| <a href='#Tabletop-Seek-Objects-InCabinet'>Tabletop-Seek-Objects-InCabinet</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Objects_InCabinet_v1_thumb_first.png' alt='Tabletop-Seek-Objects-InCabinet Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Objects_InCabinet_v1_thumb_last.png' alt='Tabletop-Seek-Objects-InCabinet Goal'> | Find the apple and the plate in the cabinet, put them on the table | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Seek_Objects_InCabinet_v1.png' alt='Tabletop-Seek-Objects-InCabinet Query'> |
| <a href='#Tabletop-Move-Cross-WithStick'>Tabletop-Move-Cross-WithStick</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cross_WithStick_v1_thumb_first.png' alt='Tabletop-Move-Cross-WithStick Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cross_WithStick_v1_thumb_last.png' alt='Tabletop-Move-Cross-WithStick Goal'> | Use the stick to move the small cube along the T-shaped path to the target position  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Cross_WithStick_v1.png' alt='Tabletop-Move-Cross-WithStick Query'> |
| <a href='#Tabletop-Find-Cube-WithPivot'>Tabletop-Find-Cube-WithPivot</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Cube_WithPivot_v1_thumb_first.png' alt='Tabletop-Find-Cube-WithPivot Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Cube_WithPivot_v1_thumb_last.png' alt='Tabletop-Find-Cube-WithPivot Goal'> | Move the heavy cube to the goal region | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Find_Cube_WithPivot_v1.png' alt='Tabletop-Find-Cube-WithPivot Query'> |
| <a href='#Tabletop-Move-Balls-WithDustpan'>Tabletop-Move-Balls-WithDustpan</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Balls_WithDustpan_v1_thumb_first.png' alt='Tabletop-Move-Balls-WithDustpan Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Balls_WithDustpan_v1_thumb_last.png' alt='Tabletop-Move-Balls-WithDustpan Goal'> | move all the balls into the holder with dustpan | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Balls_WithDustpan_v1.png' alt='Tabletop-Move-Balls-WithDustpan Query'> |
| <a href='#Tabletop-Stack-Books-OnBox'>Tabletop-Stack-Books-OnBox</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Books_OnBox_v1_thumb_first.png' alt='Tabletop-Stack-Books-OnBox Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Books_OnBox_v1_thumb_last.png' alt='Tabletop-Stack-Books-OnBox Goal'> | Stack all things on the table | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Stack_Books_OnBox_v1.png' alt='Tabletop-Stack-Books-OnBox Query'> |
| <a href='#Tabletop-Slide-Cube-Into-Container'>Tabletop-Slide-Cube-Into-Container</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Slide_Cube_Into_Container_v1_thumb_first.png' alt='Tabletop-Slide-Cube-Into-Container Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Slide_Cube_Into_Container_v1_thumb_last.png' alt='Tabletop-Slide-Cube-Into-Container Goal'> | Slide a cube down a slope into a container | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Slide_Cube_Into_Container_v1.png' alt='Tabletop-Slide-Cube-Into-Container Query'> |
| <a href='#Tabletop-Pick-Cube-WithStick'>Tabletop-Pick-Cube-WithStick</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_WithStick_v1_thumb_first.png' alt='Tabletop-Pick-Cube-WithStick Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_WithStick_v1_thumb_last.png' alt='Tabletop-Pick-Cube-WithStick Goal'> | Use the stick to move the small cube along the T-shaped path to the target position  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Cube_WithStick_v1.png' alt='Tabletop-Pick-Cube-WithStick Query'> |
| <a href='#Tabletop-Move-Cube-WithPivot'>Tabletop-Move-Cube-WithPivot</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_WithPivot_v1_thumb_first.png' alt='Tabletop-Move-Cube-WithPivot Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_WithPivot_v1_thumb_last.png' alt='Tabletop-Move-Cube-WithPivot Goal'> | move the cube with the pivot to the marker  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Cube_WithPivot_v1.png' alt='Tabletop-Move-Cube-WithPivot Query'> |
| <a href='#Tabletop-Put-Balls-IntoContainer'>Tabletop-Put-Balls-IntoContainer</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Balls_IntoContainer_v1_thumb_first.png' alt='Tabletop-Put-Balls-IntoContainer Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Balls_IntoContainer_v1_thumb_last.png' alt='Tabletop-Put-Balls-IntoContainer Goal'> | move all the balls into the dustpan as fast as you can  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Put_Balls_IntoContainer_v1.png' alt='Tabletop-Put-Balls-IntoContainer Query'> |
| <a href='#Tabletop-Insert-WithOrientation'>Tabletop-Insert-WithOrientation</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_WithOrientation_v1_thumb_first.png' alt='Tabletop-Insert-WithOrientation Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_WithOrientation_v1_thumb_last.png' alt='Tabletop-Insert-WithOrientation Goal'> | insert the board on the wall | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Insert_WithOrientation_v1.png' alt='Tabletop-Insert-WithOrientation Query'> |
| <a href='#Tabletop-Close-Door-WithObstacle'>Tabletop-Close-Door-WithObstacle</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Door_WithObstacle_v1_thumb_first.png' alt='Tabletop-Close-Door-WithObstacle Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Door_WithObstacle_v1_thumb_last.png' alt='Tabletop-Close-Door-WithObstacle Goal'> | close the door | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Close_Door_WithObstacle_v1.png' alt='Tabletop-Close-Door-WithObstacle Query'> |
| <a href='#Tabletop-Clean-For-Dinner'>Tabletop-Clean-For-Dinner</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Clean_For_Dinner_v1_thumb_first.png' alt='Tabletop-Clean-For-Dinner Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Clean_For_Dinner_v1_thumb_last.png' alt='Tabletop-Clean-For-Dinner Goal'> | Arrange the bowl, fork onto the plate, clean for dinner  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Clean_For_Dinner_v1.png' alt='Tabletop-Clean-For-Dinner Query'> |
| <a href='#Tabletop-Pick-Cube-Slippery'>Tabletop-Pick-Cube-Slippery</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_Slippery_v1_thumb_first.png' alt='Tabletop-Pick-Cube-Slippery Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_Slippery_v1_thumb_last.png' alt='Tabletop-Pick-Cube-Slippery Goal'> | Pick the slippery cube  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Cube_Slippery_v1.png' alt='Tabletop-Pick-Cube-Slippery Query'> |
| <a href='#Tabletop-Move-Balls-WithPivot'>Tabletop-Move-Balls-WithPivot</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Balls_WithPivot_v1_thumb_first.png' alt='Tabletop-Move-Balls-WithPivot Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Balls_WithPivot_v1_thumb_last.png' alt='Tabletop-Move-Balls-WithPivot Goal'> | move all the balls into the dustpan as fast as you can  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Balls_WithPivot_v1.png' alt='Tabletop-Move-Balls-WithPivot Query'> |
| <a href='#Tabletop-Open-Door-WithCabinet'>Tabletop-Open-Door-WithCabinet</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_WithCabinet_v1_thumb_first.png' alt='Tabletop-Open-Door-WithCabinet Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_WithCabinet_v1_thumb_last.png' alt='Tabletop-Open-Door-WithCabinet Goal'> | open the door | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Open_Door_WithCabinet_v1.png' alt='Tabletop-Open-Door-WithCabinet Query'> |
| <a href='#Tabletop-Open-Cabinet-WithObstacle'>Tabletop-Open-Cabinet-WithObstacle</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithObstacle_v1_thumb_first.png' alt='Tabletop-Open-Cabinet-WithObstacle Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithObstacle_v1_thumb_last.png' alt='Tabletop-Open-Cabinet-WithObstacle Goal'> | open the cabinet door | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Open_Cabinet_WithObstacle_v1.png' alt='Tabletop-Open-Cabinet-WithObstacle Query'> |
| <a href='#Tabletop-Pick-Object-FromCabinet'>Tabletop-Pick-Object-FromCabinet</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Object_FromCabinet_v1_thumb_first.png' alt='Tabletop-Pick-Object-FromCabinet Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Object_FromCabinet_v1_thumb_last.png' alt='Tabletop-Pick-Object-FromCabinet Goal'> | pick up the object from the cabinet  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Object_FromCabinet_v1.png' alt='Tabletop-Pick-Object-FromCabinet Query'> |
| <a href='#Tabletop-Stack-Books'>Tabletop-Stack-Books</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Books_v1_thumb_first.png' alt='Tabletop-Stack-Books Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Books_v1_thumb_last.png' alt='Tabletop-Stack-Books Goal'> | Stack all things on the table | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Stack_Books_v1.png' alt='Tabletop-Stack-Books Query'> |
| <a href='#Tabletop-Insert-Conical'>Tabletop-Insert-Conical</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_Conical_v1_thumb_first.png' alt='Tabletop-Insert-Conical Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_Conical_v1_thumb_last.png' alt='Tabletop-Insert-Conical Goal'> | insert the conical to the container | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Insert_Conical_v1.png' alt='Tabletop-Insert-Conical Query'> |
| <a href='#Tabletop-Put-Cube-IntoMicrowave'>Tabletop-Put-Cube-IntoMicrowave</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Cube_IntoMicrowave_v1_thumb_first.png' alt='Tabletop-Put-Cube-IntoMicrowave Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Cube_IntoMicrowave_v1_thumb_last.png' alt='Tabletop-Put-Cube-IntoMicrowave Goal'> | put the cube into the microwave  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Put_Cube_IntoMicrowave_v1.png' alt='Tabletop-Put-Cube-IntoMicrowave Query'> |
| <a href='#Tabletop-Pick-Cylinder-WithObstacle'>Tabletop-Pick-Cylinder-WithObstacle</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cylinder_WithObstacle_v1_thumb_first.png' alt='Tabletop-Pick-Cylinder-WithObstacle Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cylinder_WithObstacle_v1_thumb_last.png' alt='Tabletop-Pick-Cylinder-WithObstacle Goal'> | pick up the center cylinder | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Cylinder_WithObstacle_v1.png' alt='Tabletop-Pick-Cylinder-WithObstacle Query'> |
| <a href='#Tabletop-Keep-Pivot-Balance'>Tabletop-Keep-Pivot-Balance</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Keep_Pivot_Balance_v1_thumb_first.png' alt='Tabletop-Keep-Pivot-Balance Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Keep_Pivot_Balance_v1_thumb_last.png' alt='Tabletop-Keep-Pivot-Balance Goal'> | Balance the long board on the triangular prism and place the cubes to maintain balance | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Keep_Pivot_Balance_v1.png' alt='Tabletop-Keep-Pivot-Balance Query'> |
| <a href='#Tabletop-Move-Line-WithStick'>Tabletop-Move-Line-WithStick</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Line_WithStick_v1_thumb_first.png' alt='Tabletop-Move-Line-WithStick Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Line_WithStick_v1_thumb_last.png' alt='Tabletop-Move-Line-WithStick Goal'> | Use the stick to move the small cube along the straight line path to the target position  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Line_WithStick_v1.png' alt='Tabletop-Move-Line-WithStick Query'> |
| <a href='#Tabletop-Slide-Cube-WithPath'>Tabletop-Slide-Cube-WithPath</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Slide_Cube_WithPath_v1_thumb_first.png' alt='Tabletop-Slide-Cube-WithPath Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Slide_Cube_WithPath_v1_thumb_last.png' alt='Tabletop-Slide-Cube-WithPath Goal'> | Slide a cube down a slope to the target position  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Slide_Cube_WithPath_v1.png' alt='Tabletop-Slide-Cube-WithPath Query'> |
| <a href='#Tabletop-Finish-Hanobi'>Tabletop-Finish-Hanobi</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Finish_Hanobi_v1_thumb_first.png' alt='Tabletop-Finish-Hanobi Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Finish_Hanobi_v1_thumb_last.png' alt='Tabletop-Finish-Hanobi Goal'> | Place all the hanobi in big to small from bottom to up | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Finish_Hanobi_v1.png' alt='Tabletop-Finish-Hanobi Query'> |
| <a href='#Tabletop-Pick-Cube-WithDoor'>Tabletop-Pick-Cube-WithDoor</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_WithDoor_v1_thumb_first.png' alt='Tabletop-Pick-Cube-WithDoor Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_WithDoor_v1_thumb_last.png' alt='Tabletop-Pick-Cube-WithDoor Goal'> | put the cube to the marker | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Cube_WithDoor_v1.png' alt='Tabletop-Pick-Cube-WithDoor Query'> |
| <a href='#Tabletop-Move-Cube-WithHolder'>Tabletop-Move-Cube-WithHolder</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_WithHolder_v1_thumb_first.png' alt='Tabletop-Move-Cube-WithHolder Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_WithHolder_v1_thumb_last.png' alt='Tabletop-Move-Cube-WithHolder Goal'> | move the cube to the marker and put the holder on the cube  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Cube_WithHolder_v1.png' alt='Tabletop-Move-Cube-WithHolder Query'> |
| <a href='#Tabletop-Find-Book-FromShelf'>Tabletop-Find-Book-FromShelf</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Book_FromShelf_v1_thumb_first.png' alt='Tabletop-Find-Book-FromShelf Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Book_FromShelf_v1_thumb_last.png' alt='Tabletop-Find-Book-FromShelf Goal'> | Find and pick the highest book from the bookshelf and put it on the marker  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Find_Book_FromShelf_v1.png' alt='Tabletop-Find-Book-FromShelf Query'> |
| <a href='#Tabletop-Rotate-Cube-Twice'>Tabletop-Rotate-Cube-Twice</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Cube_Twice_v1_thumb_first.png' alt='Tabletop-Rotate-Cube-Twice Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Cube_Twice_v1_thumb_last.png' alt='Tabletop-Rotate-Cube-Twice Goal'> | rotate the cube till the green face upward | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Rotate_Cube_Twice_v1.png' alt='Tabletop-Rotate-Cube-Twice Query'> |
| <a href='#Tabletop-Insert-Objects-WithShape'>Tabletop-Insert-Objects-WithShape</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_Objects_WithShape_v1_thumb_first.png' alt='Tabletop-Insert-Objects-WithShape Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_Objects_WithShape_v1_thumb_last.png' alt='Tabletop-Insert-Objects-WithShape Goal'> | insert all the stick on the table into corresponding holes | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Insert_Objects_WithShape_v1.png' alt='Tabletop-Insert-Objects-WithShape Query'> |
| <a href='#Tabletop-Merge-USB'>Tabletop-Merge-USB</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Merge_USB_v1_thumb_first.png' alt='Tabletop-Merge-USB Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Merge_USB_v1_thumb_last.png' alt='Tabletop-Merge-USB Goal'> | Pick up the USB body and insert it into the USB hub | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Merge_USB_v1.png' alt='Tabletop-Merge-USB Query'> |
| <a href='#Tabletop-Pick-Eraser-FromHolder'>Tabletop-Pick-Eraser-FromHolder</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Eraser_FromHolder_v1_thumb_first.png' alt='Tabletop-Pick-Eraser-FromHolder Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Eraser_FromHolder_v1_thumb_last.png' alt='Tabletop-Pick-Eraser-FromHolder Goal'> | Pick up the eraser in the holder and place it to the marker | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Eraser_FromHolder_v1.png' alt='Tabletop-Pick-Eraser-FromHolder Query'> |
| <a href='#Tabletop-Move-Cube-DynamicFriction'>Tabletop-Move-Cube-DynamicFriction</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_DynamicFriction_v1_thumb_first.png' alt='Tabletop-Move-Cube-DynamicFriction Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_DynamicFriction_v1_thumb_last.png' alt='Tabletop-Move-Cube-DynamicFriction Goal'> | move the cube to the marker | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Cube_DynamicFriction_v1.png' alt='Tabletop-Move-Cube-DynamicFriction Query'> |
| <a href='#Tabletop-Find-Cube-RedDown'>Tabletop-Find-Cube-RedDown</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Cube_RedDown_v1_thumb_first.png' alt='Tabletop-Find-Cube-RedDown Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Cube_RedDown_v1_thumb_last.png' alt='Tabletop-Find-Cube-RedDown Goal'> | find the cube which have red face downward, and put it on the marker with red face upward | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Find_Cube_RedDown_v1.png' alt='Tabletop-Find-Cube-RedDown Query'> |
| <a href='#Tabletop-Merge-Box'>Tabletop-Merge-Box</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Merge_Box_v1_thumb_first.png' alt='Tabletop-Merge-Box Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Merge_Box_v1_thumb_last.png' alt='Tabletop-Merge-Box Goal'> | Merge ball and boxs up  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Merge_Box_v1.png' alt='Tabletop-Merge-Box Query'> |
| <a href='#Tabletop-Open-Cabinet-WithDoor'>Tabletop-Open-Cabinet-WithDoor</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithDoor_v1_thumb_first.png' alt='Tabletop-Open-Cabinet-WithDoor Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithDoor_v1_thumb_last.png' alt='Tabletop-Open-Cabinet-WithDoor Goal'> | open the cabinet door | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Open_Cabinet_WithDoor_v1.png' alt='Tabletop-Open-Cabinet-WithDoor Query'> |
| <a href='#Tabletop-Open-Cabinet-WithSwitch'>Tabletop-Open-Cabinet-WithSwitch</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithSwitch_v1_thumb_first.png' alt='Tabletop-Open-Cabinet-WithSwitch Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithSwitch_v1_thumb_last.png' alt='Tabletop-Open-Cabinet-WithSwitch Goal'> | open the door, notice the switch will control the state of the door  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Open_Cabinet_WithSwitch_v1.png' alt='Tabletop-Open-Cabinet-WithSwitch Query'> |
| <a href='#Tabletop-Close-Drawer-WithObstacle'>Tabletop-Close-Drawer-WithObstacle</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_WithObstacle_v1_thumb_first.png' alt='Tabletop-Close-Drawer-WithObstacle Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_WithObstacle_v1_thumb_last.png' alt='Tabletop-Close-Drawer-WithObstacle Goal'> | close the drawer | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Close_Drawer_WithObstacle_v1.png' alt='Tabletop-Close-Drawer-WithObstacle Query'> |
| <a href='#Tabletop-Find-Book-Black'>Tabletop-Find-Book-Black</a> | Interactive | ✓ | ✓ | ✓ | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Book_Black_v1_thumb_first.png' alt='Tabletop-Find-Book-Black Initial'> | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Book_Black_v1_thumb_last.png' alt='Tabletop-Find-Book-Black Goal'> | Find and pick the black book from the bookshelf and put it on the marker  | <img style='width:100%;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Find_Book_Black_v1.png' alt='Tabletop-Find-Book-Black Query'> |

### Tabletop-Balance-Pivot-WithBalls

**Environment ID:** `Tabletop-Balance-Pivot-WithBalls-v1`

**Instruction:** Balance the long board on the triangular prism and place the cubes to maintain balance

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Balance_Pivot_WithBalls_v1_thumb_first.png' alt='Tabletop-Balance-Pivot-WithBalls Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Balance_Pivot_WithBalls_v1_thumb_last.png' alt='Tabletop-Balance-Pivot-WithBalls Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Balance_Pivot_WithBalls_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** How many balls can make the pivot balance?

**Options:**
A: 4
B: 5
C: 6

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Balance_Pivot_WithBalls.png' alt='Tabletop-Balance-Pivot-WithBalls Query'>

### Tabletop-Open-Door-WithObstacle

**Environment ID:** `Tabletop-Open-Door-WithObstacle-v1`

**Instruction:** open the door

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_WithObstacle_v1_thumb_first.png' alt='Tabletop-Open-Door-WithObstacle Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_WithObstacle_v1_thumb_last.png' alt='Tabletop-Open-Door-WithObstacle Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_WithObstacle_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the main challenge in opening this door?

**Options:**
A: The door is unreachable
B: The door is too heavy to be opened directly
C: There is an obstacle blocking the door's path

**Answer:** C
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Open_Door_WithObstacle.png' alt='Tabletop-Open-Door-WithObstacle Query'>

### Tabletop-Find-Dice

**Environment ID:** `Tabletop-Find-Dice-v1`

**Instruction:** find the dice which have 2 and 4 point in the corresponding face and put it on the marker

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Dice_v1_thumb_first.png' alt='Tabletop-Find-Dice Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Dice_v1_thumb_last.png' alt='Tabletop-Find-Dice Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Dice_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** which dice has 2 and 4 point in the corresponding face

**Options:**
A: A
B: B

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Find_Dice.png' alt='Tabletop-Find-Dice Query'>

### Tabletop-Seek-Holder-InCabinet

**Environment ID:** `Tabletop-Seek-Holder-InCabinet-v1`

**Instruction:** Find the holder containing an eraser the cabinet, put it to the marker

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Holder_InCabinet_v1_thumb_first.png' alt='Tabletop-Seek-Holder-InCabinet Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Holder_InCabinet_v1_thumb_last.png' alt='Tabletop-Seek-Holder-InCabinet Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Holder_InCabinet_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Which holder has a eraser?

**Options:**
A: A
B: B

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Seek_Holder_InCabinet.png' alt='Tabletop-Seek-Holder-InCabinet Query'>

### Tabletop-Stack-Cube-WithColor

**Environment ID:** `Tabletop-Stack-Cube-WithColor-v1`

**Instruction:** Stack the cube with same color

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Cube_WithColor_v1_thumb_first.png' alt='Tabletop-Stack-Cube-WithColor Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Cube_WithColor_v1_thumb_last.png' alt='Tabletop-Stack-Cube-WithColor Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Cube_WithColor_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** How many degrees should A be rotated along y axis(the axis vertical to the white face) to make it same color with B?

**Options:**
A: 90
B: 180
C: 270

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Stack_Cube_WithColor.png' alt='Tabletop-Stack-Cube-WithColor Query'>

### Tabletop-Stack-LongObjects

**Environment ID:** `Tabletop-Stack-LongObjects-v1`

**Instruction:** stack all the objects to make it most high

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_LongObjects_v1_thumb_first.png' alt='Tabletop-Stack-LongObjects Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_LongObjects_v1_thumb_last.png' alt='Tabletop-Stack-LongObjects Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_LongObjects_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Which cube is the highest?

**Options:**
A: A
B: B
C: C

**Answer:** C
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Stack_LongObjects.png' alt='Tabletop-Stack-LongObjects Query'>

### Tabletop-Put-Cube-IntoCabinetWithObstacle

**Environment ID:** `Tabletop-Put-Cube-IntoCabinetWithObstacle-v1`

**Instruction:**  put the object into the cabinet

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Cube_IntoCabinetWithObstacle_v1_thumb_first.png' alt='Tabletop-Put-Cube-IntoCabinetWithObstacle Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Cube_IntoCabinetWithObstacle_v1_thumb_last.png' alt='Tabletop-Put-Cube-IntoCabinetWithObstacle Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Cube_IntoCabinetWithObstacle_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the best approach to put the cube into the cabinet

**Options:**
A: Move the obstacle first, then place the cube into the cabinet
B: Try to navigate around the obstacle without moving it

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Put_Cube_IntoCabinetWithObstacle.png' alt='Tabletop-Put-Cube-IntoCabinetWithObstacle Query'>

### Tabletop-Lift-Book

**Environment ID:** `Tabletop-Lift-Book-v1`

**Instruction:** lift the book up to the higher platform

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Lift_Book_v1_thumb_first.png' alt='Tabletop-Lift-Book Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Lift_Book_v1_thumb_last.png' alt='Tabletop-Lift-Book Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Lift_Book_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** How to move the book to the higher platform?

**Options:**
A: Directly grasp the book and lift it up to the higher platform
B: Push the book to create an overhang at the table edge, then grasp and lift
C: Attempt to slide fingers underneath the book without creating an overhang first

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Lift_Book.png' alt='Tabletop-Lift-Book Query'>

### Tabletop-Close-Cabinet-WithObstacle

**Environment ID:** `Tabletop-Close-Cabinet-WithObstacle-v1`

**Instruction:** open the cabinet door

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Cabinet_WithObstacle_v1_thumb_first.png' alt='Tabletop-Close-Cabinet-WithObstacle Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Cabinet_WithObstacle_v1_thumb_last.png' alt='Tabletop-Close-Cabinet-WithObstacle Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Cabinet_WithObstacle_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Which approach would most likely succeed in closing the cabinet?

**Options:**
A: Apply force directly to the door
B: Move the obstacle first, then close the door

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Close_Cabinet_WithObstacle.png' alt='Tabletop-Close-Cabinet-WithObstacle Query'>

### Tabletop-Seek-Objects-WithObstacle

**Environment ID:** `Tabletop-Seek-Objects-WithObstacle-v1`

**Instruction:** find the cube in the cabinet and pick it up

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Objects_WithObstacle_v1_thumb_first.png' alt='Tabletop-Seek-Objects-WithObstacle Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Objects_WithObstacle_v1_thumb_last.png' alt='Tabletop-Seek-Objects-WithObstacle Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Objects_WithObstacle_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Where is the cube?

**Options:**
A: In the drawer
B: In the cabinet

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Seek_Objects_WithObstacle.png' alt='Tabletop-Seek-Objects-WithObstacle Query'>

### Tabletop-Close-Drawer-WithLongObstacle

**Environment ID:** `Tabletop-Close-Drawer-WithLongObstacle-v1`

**Instruction:** close the drawer

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_WithLongObstacle_v1_thumb_first.png' alt='Tabletop-Close-Drawer-WithLongObstacle Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_WithLongObstacle_v1_thumb_last.png' alt='Tabletop-Close-Drawer-WithLongObstacle Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_WithLongObstacle_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What's the best approach to close the drawer?

**Options:**
A: Push the drawer directly
B: Remove the red obstacle first, then close the drawer

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Close_Drawer_WithLongObstacle.png' alt='Tabletop-Close-Drawer-WithLongObstacle Query'>

### Tabletop-Seek-Objects-InCabinet

**Environment ID:** `Tabletop-Seek-Objects-InCabinet-v1`

**Instruction:** Find the apple and the plate in the cabinet, put them on the table

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Objects_InCabinet_v1_thumb_first.png' alt='Tabletop-Seek-Objects-InCabinet Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Objects_InCabinet_v1_thumb_last.png' alt='Tabletop-Seek-Objects-InCabinet Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Seek_Objects_InCabinet_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Where are the apple and plate?

**Options:**
A: The apple is in the drawer, the plate is in cabinet
B: The apple is in the cabinet, the plate is in drawer
C: Both of the are in cabinet
D: Both of the are in drawer

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Seek_Objects_InCabinet.png' alt='Tabletop-Seek-Objects-InCabinet Query'>

### Tabletop-Move-Cross-WithStick

**Environment ID:** `Tabletop-Move-Cross-WithStick-v1`

**Instruction:** Use the stick to move the small cube along the T-shaped path to the target position

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cross_WithStick_v1_thumb_first.png' alt='Tabletop-Move-Cross-WithStick Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cross_WithStick_v1_thumb_last.png' alt='Tabletop-Move-Cross-WithStick Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cross_WithStick_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** How should the robot navigate the cube through the T-junction?

**Options:**
A: Push the cube to the junction with stick, then reposition the stick for the turn
B: Directly pick up the cube to the target position

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Cross_WithStick.png' alt='Tabletop-Move-Cross-WithStick Query'>

### Tabletop-Find-Cube-WithPivot

**Environment ID:** `Tabletop-Find-Cube-WithPivot-v1`

**Instruction:** Move the heavy cube to the goal region

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Cube_WithPivot_v1_thumb_first.png' alt='Tabletop-Find-Cube-WithPivot Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Cube_WithPivot_v1_thumb_last.png' alt='Tabletop-Find-Cube-WithPivot Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Cube_WithPivot_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** which cube is heavier

**Options:**
A: A
B: B

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Find_Cube_WithPivot.png' alt='Tabletop-Find-Cube-WithPivot Query'>

### Tabletop-Move-Balls-WithDustpan

**Environment ID:** `Tabletop-Move-Balls-WithDustpan-v1`

**Instruction:** move all the balls into the holder with dustpan

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Balls_WithDustpan_v1_thumb_first.png' alt='Tabletop-Move-Balls-WithDustpan Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Balls_WithDustpan_v1_thumb_last.png' alt='Tabletop-Move-Balls-WithDustpan Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Balls_WithDustpan_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What strategy should be used to collect multiple balls efficiently?

**Options:**
A: Collect all balls at once with a single sweeping motion
B: Move the balls one by one

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Balls_WithDustpan.png' alt='Tabletop-Move-Balls-WithDustpan Query'>

### Tabletop-Stack-Books-OnBox

**Environment ID:** `Tabletop-Stack-Books-OnBox-v1`

**Instruction:** Stack all things on the table

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Books_OnBox_v1_thumb_first.png' alt='Tabletop-Stack-Books-OnBox Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Books_OnBox_v1_thumb_last.png' alt='Tabletop-Stack-Books-OnBox Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Books_OnBox_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Which book should be stacked on top of the other?

**Options:**
A: The red book should be placed on top of the green book
B: The green book should be placed on top of the red book

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Stack_Books_OnBox.png' alt='Tabletop-Stack-Books-OnBox Query'>

### Tabletop-Slide-Cube-Into-Container

**Environment ID:** `Tabletop-Slide-Cube-Into-Container-v1`

**Instruction:** Slide a cube down a slope into a container

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Slide_Cube_Into_Container_v1_thumb_first.png' alt='Tabletop-Slide-Cube-Into-Container Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Slide_Cube_Into_Container_v1_thumb_last.png' alt='Tabletop-Slide-Cube-Into-Container Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Slide_Cube_Into_Container_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** How can we put the cube to the container?

**Options:**
A: Slide it from the top of the slope
B: Put the cube to the dustpan directly

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Slide_Cube_Into_Container.png' alt='Tabletop-Slide-Cube-Into-Container Query'>

### Tabletop-Pick-Cube-WithStick

**Environment ID:** `Tabletop-Pick-Cube-WithStick-v1`

**Instruction:** Use the stick to move the small cube along the T-shaped path to the target position

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_WithStick_v1_thumb_first.png' alt='Tabletop-Pick-Cube-WithStick Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_WithStick_v1_thumb_last.png' alt='Tabletop-Pick-Cube-WithStick Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_WithStick_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Why we need a stick to move the cube?

**Options:**
A: Because the cube is too small and the path is too narrow
B: Because the cube is too heavy to move
C: Because the cube is too slippery

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Cube_WithStick.png' alt='Tabletop-Pick-Cube-WithStick Query'>

### Tabletop-Move-Cube-WithPivot

**Environment ID:** `Tabletop-Move-Cube-WithPivot-v1`

**Instruction:** move the cube with the pivot to the marker

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_WithPivot_v1_thumb_first.png' alt='Tabletop-Move-Cube-WithPivot Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_WithPivot_v1_thumb_last.png' alt='Tabletop-Move-Cube-WithPivot Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_WithPivot_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Why we need the pivot to move the cube?

**Options:**
A: The cube is too heavy to lift
B: The cube is too far to grasp
C: The pivot is decorative and serves no functional purpose

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Cube_WithPivot.png' alt='Tabletop-Move-Cube-WithPivot Query'>

### Tabletop-Put-Balls-IntoContainer

**Environment ID:** `Tabletop-Put-Balls-IntoContainer-v1`

**Instruction:** move all the balls into the dustpan as fast as you can

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Balls_IntoContainer_v1_thumb_first.png' alt='Tabletop-Put-Balls-IntoContainer Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Balls_IntoContainer_v1_thumb_last.png' alt='Tabletop-Put-Balls-IntoContainer Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Balls_IntoContainer_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the most efficient way to get all the balls into the dustpan?

**Options:**
A: Pick up and place each ball individually into the dustpan
B: Push multiple balls at once with arm

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Put_Balls_IntoContainer.png' alt='Tabletop-Put-Balls-IntoContainer Query'>

### Tabletop-Insert-WithOrientation

**Environment ID:** `Tabletop-Insert-WithOrientation-v1`

**Instruction:** insert the board on the wall

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_WithOrientation_v1_thumb_first.png' alt='Tabletop-Insert-WithOrientation Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_WithOrientation_v1_thumb_last.png' alt='Tabletop-Insert-WithOrientation Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_WithOrientation_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the correct orientation for inserting the blue object?

**Options:**
A: Rotate the object vertically to match the slot height
B: Keep the object flat on the table and push it in

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Insert_WithOrientation.png' alt='Tabletop-Insert-WithOrientation Query'>

### Tabletop-Close-Door-WithObstacle

**Environment ID:** `Tabletop-Close-Door-WithObstacle-v1`

**Instruction:** close the door

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Door_WithObstacle_v1_thumb_first.png' alt='Tabletop-Close-Door-WithObstacle Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Door_WithObstacle_v1_thumb_last.png' alt='Tabletop-Close-Door-WithObstacle Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Door_WithObstacle_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What should be done first to close the door?

**Options:**
A: Grasp and move the bowl
B: Push the door handle directly

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Close_Door_WithObstacle.png' alt='Tabletop-Close-Door-WithObstacle Query'>

### Tabletop-Clean-For-Dinner

**Environment ID:** `Tabletop-Clean-For-Dinner-v1`

**Instruction:** Arrange the bowl, fork onto the plate, clean for dinner

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Clean_For_Dinner_v1_thumb_first.png' alt='Tabletop-Clean-For-Dinner Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Clean_For_Dinner_v1_thumb_last.png' alt='Tabletop-Clean-For-Dinner Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Clean_For_Dinner_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Which item should be placed on the plate first?

**Options:**
A: The bowl
B: The fork

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Clean_For_Dinner.png' alt='Tabletop-Clean-For-Dinner Query'>

### Tabletop-Pick-Cube-Slippery

**Environment ID:** `Tabletop-Pick-Cube-Slippery-v1`

**Instruction:** Pick the slippery cube

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_Slippery_v1_thumb_first.png' alt='Tabletop-Pick-Cube-Slippery Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_Slippery_v1_thumb_last.png' alt='Tabletop-Pick-Cube-Slippery Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_Slippery_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Which cube is slippery?

**Options:**
A: A
B: B

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Cube_Slippery.png' alt='Tabletop-Pick-Cube-Slippery Query'>

### Tabletop-Move-Balls-WithPivot

**Environment ID:** `Tabletop-Move-Balls-WithPivot-v1`

**Instruction:** move all the balls into the dustpan as fast as you can

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Balls_WithPivot_v1_thumb_first.png' alt='Tabletop-Move-Balls-WithPivot Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Balls_WithPivot_v1_thumb_last.png' alt='Tabletop-Move-Balls-WithPivot Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Balls_WithPivot_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the most efficient way to collect all the balls?

**Options:**
A: Pick the balls to the dustpan one by one
B: Use the pivot to collect all the balls

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Balls_WithPivot.png' alt='Tabletop-Move-Balls-WithPivot Query'>

### Tabletop-Open-Door-WithCabinet

**Environment ID:** `Tabletop-Open-Door-WithCabinet-v1`

**Instruction:** open the door

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_WithCabinet_v1_thumb_first.png' alt='Tabletop-Open-Door-WithCabinet Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_WithCabinet_v1_thumb_last.png' alt='Tabletop-Open-Door-WithCabinet Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Door_WithCabinet_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the main challenge in opening this door?

**Options:**
A: The door is too heavy to push
B: The cabinet door is in the way to open the door
C: We can directly open the door

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Open_Door_WithCabinet.png' alt='Tabletop-Open-Door-WithCabinet Query'>

### Tabletop-Open-Cabinet-WithObstacle

**Environment ID:** `Tabletop-Open-Cabinet-WithObstacle-v1`

**Instruction:** open the cabinet door

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithObstacle_v1_thumb_first.png' alt='Tabletop-Open-Cabinet-WithObstacle Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithObstacle_v1_thumb_last.png' alt='Tabletop-Open-Cabinet-WithObstacle Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithObstacle_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the efficient way to open the cabinet

**Options:**
A: Move the board away, then open the cabinet
B: Open the cabinet directly

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Open_Cabinet_WithObstacle.png' alt='Tabletop-Open-Cabinet-WithObstacle Query'>

### Tabletop-Pick-Object-FromCabinet

**Environment ID:** `Tabletop-Pick-Object-FromCabinet-v1`

**Instruction:** pick up the object from the cabinet

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Object_FromCabinet_v1_thumb_first.png' alt='Tabletop-Pick-Object-FromCabinet Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Object_FromCabinet_v1_thumb_last.png' alt='Tabletop-Pick-Object-FromCabinet Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Object_FromCabinet_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What's the object in the cabinet?

**Options:**
A: A book
B: A cube
C: A pen

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Object_FromCabinet.png' alt='Tabletop-Pick-Object-FromCabinet Query'>

### Tabletop-Stack-Books

**Environment ID:** `Tabletop-Stack-Books-v1`

**Instruction:** Stack all things on the table

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Books_v1_thumb_first.png' alt='Tabletop-Stack-Books Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Books_v1_thumb_last.png' alt='Tabletop-Stack-Books Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Stack_Books_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Which book should be stacked on top of the other?

**Options:**
A: The red book should be placed on top of the green book
B: The green book should be placed on top of the red book

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Stack_Books.png' alt='Tabletop-Stack-Books Query'>

### Tabletop-Insert-Conical

**Environment ID:** `Tabletop-Insert-Conical-v1`

**Instruction:** insert the conical to the container

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_Conical_v1_thumb_first.png' alt='Tabletop-Insert-Conical Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_Conical_v1_thumb_last.png' alt='Tabletop-Insert-Conical Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_Conical_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What to prevent while insert the water bottle

**Options:**
A: Tilting the bottle too much, which may cause misalignment
B: Moving too slowly, which wastes time and energy

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Insert_Conical.png' alt='Tabletop-Insert-Conical Query'>

### Tabletop-Put-Cube-IntoMicrowave

**Environment ID:** `Tabletop-Put-Cube-IntoMicrowave-v1`

**Instruction:** put the cube into the microwave

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Cube_IntoMicrowave_v1_thumb_first.png' alt='Tabletop-Put-Cube-IntoMicrowave Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Cube_IntoMicrowave_v1_thumb_last.png' alt='Tabletop-Put-Cube-IntoMicrowave Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Put_Cube_IntoMicrowave_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the correct order of actions to put the cube into the microwave?

**Options:**
A: Pick up the cube first, then open the microwave door and place the cube inside
B: Open the microwave door first, then pick and place the cube inside
C: Directly pick the cube into microwave

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Put_Cube_IntoMicrowave.png' alt='Tabletop-Put-Cube-IntoMicrowave Query'>

### Tabletop-Pick-Cylinder-WithObstacle

**Environment ID:** `Tabletop-Pick-Cylinder-WithObstacle-v1`

**Instruction:** pick up the center cylinder

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cylinder_WithObstacle_v1_thumb_first.png' alt='Tabletop-Pick-Cylinder-WithObstacle Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cylinder_WithObstacle_v1_thumb_last.png' alt='Tabletop-Pick-Cylinder-WithObstacle Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cylinder_WithObstacle_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** How to move the center cylinder to the goal?

**Options:**
A: Pick up the center cylinder directly and move it to the goal
B: Find the dynamic obstacle cylinders and push them away to move the center cylinder to the goal
C: Put one of the dynamic cylinder to the goal

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Cylinder_WithObstacle.png' alt='Tabletop-Pick-Cylinder-WithObstacle Query'>

### Tabletop-Keep-Pivot-Balance

**Environment ID:** `Tabletop-Keep-Pivot-Balance-v1`

**Instruction:** Balance the long board on the triangular prism and place the cubes to maintain balance

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Keep_Pivot_Balance_v1_thumb_first.png' alt='Tabletop-Keep-Pivot-Balance Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Keep_Pivot_Balance_v1_thumb_last.png' alt='Tabletop-Keep-Pivot-Balance Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Keep_Pivot_Balance_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** which cube is heavier

**Options:**
A: Cube A
B: Cube B

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Keep_Pivot_Balance.png' alt='Tabletop-Keep-Pivot-Balance Query'>

### Tabletop-Move-Line-WithStick

**Environment ID:** `Tabletop-Move-Line-WithStick-v1`

**Instruction:** Use the stick to move the small cube along the straight line path to the target position

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Line_WithStick_v1_thumb_first.png' alt='Tabletop-Move-Line-WithStick Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Line_WithStick_v1_thumb_last.png' alt='Tabletop-Move-Line-WithStick Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Line_WithStick_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What approach should be used to move the cube along the path?

**Options:**
A: Use the stick to push the cube
B: Directly push the cube with continuous contact
C: Pick the cube up and place it to the target

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Line_WithStick.png' alt='Tabletop-Move-Line-WithStick Query'>

### Tabletop-Slide-Cube-WithPath

**Environment ID:** `Tabletop-Slide-Cube-WithPath-v1`

**Instruction:** Slide a cube down a slope to the target position

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Slide_Cube_WithPath_v1_thumb_first.png' alt='Tabletop-Slide-Cube-WithPath Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Slide_Cube_WithPath_v1_thumb_last.png' alt='Tabletop-Slide-Cube-WithPath Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Slide_Cube_WithPath_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Where should the block be placed to slide to target position?

**Options:**
A: A
B: B

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Slide_Cube_WithPath.png' alt='Tabletop-Slide-Cube-WithPath Query'>

### Tabletop-Finish-Hanobi

**Environment ID:** `Tabletop-Finish-Hanobi-v1`

**Instruction:** Place all the hanobi in big to small from bottom to up

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Finish_Hanobi_v1_thumb_first.png' alt='Tabletop-Finish-Hanobi Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Finish_Hanobi_v1_thumb_last.png' alt='Tabletop-Finish-Hanobi Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Finish_Hanobi_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the size order of the yellow, red, and blue hanoi?

**Options:**
A: Yellow > Blue > Red
B: Red > Yellow > Blue
C: Blue > Yellow > Red

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Finish_Hanobi.png' alt='Tabletop-Finish-Hanobi Query'>

### Tabletop-Pick-Cube-WithDoor

**Environment ID:** `Tabletop-Pick-Cube-WithDoor-v1`

**Instruction:** put the cube to the marker

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_WithDoor_v1_thumb_first.png' alt='Tabletop-Pick-Cube-WithDoor Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_WithDoor_v1_thumb_last.png' alt='Tabletop-Pick-Cube-WithDoor Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Cube_WithDoor_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the correct sequence to retrieve the cube?

**Options:**
A: Reach for the cube without opening the door
B: Open the door first, then pick the cube

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Cube_WithDoor.png' alt='Tabletop-Pick-Cube-WithDoor Query'>

### Tabletop-Move-Cube-WithHolder

**Environment ID:** `Tabletop-Move-Cube-WithHolder-v1`

**Instruction:** move the cube to the marker and put the holder on the cube

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_WithHolder_v1_thumb_first.png' alt='Tabletop-Move-Cube-WithHolder Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_WithHolder_v1_thumb_last.png' alt='Tabletop-Move-Cube-WithHolder Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_WithHolder_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What's the best sequence of actions for this task?

**Options:**
A: Move the cube to the marker first, then place the holder on top
B: Move the holder first, then place the cube to the marker, finally put the holder on the cube

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Cube_WithHolder.png' alt='Tabletop-Move-Cube-WithHolder Query'>

### Tabletop-Find-Book-FromShelf

**Environment ID:** `Tabletop-Find-Book-FromShelf-v1`

**Instruction:** Find and pick the highest book from the bookshelf and put it on the marker

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Book_FromShelf_v1_thumb_first.png' alt='Tabletop-Find-Book-FromShelf Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Book_FromShelf_v1_thumb_last.png' alt='Tabletop-Find-Book-FromShelf Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Book_FromShelf_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** which is the highest book

**Options:**
A: A
B: B
C: C

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Find_Book_FromShelf.png' alt='Tabletop-Find-Book-FromShelf Query'>

### Tabletop-Rotate-Cube-Twice

**Environment ID:** `Tabletop-Rotate-Cube-Twice-v1`

**Instruction:** rotate the cube till the green face upward

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Cube_Twice_v1_thumb_first.png' alt='Tabletop-Rotate-Cube-Twice Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Cube_Twice_v1_thumb_last.png' alt='Tabletop-Rotate-Cube-Twice Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Rotate_Cube_Twice_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Where is the green face?

**Options:**
A: On the top of the cube
B: On the side of the cube
C: On the bottom of the cube

**Answer:** C
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Rotate_Cube_Twice.png' alt='Tabletop-Rotate-Cube-Twice Query'>

### Tabletop-Insert-Objects-WithShape

**Environment ID:** `Tabletop-Insert-Objects-WithShape-v1`

**Instruction:** insert all the stick on the table into corresponding holes

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_Objects_WithShape_v1_thumb_first.png' alt='Tabletop-Insert-Objects-WithShape Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_Objects_WithShape_v1_thumb_last.png' alt='Tabletop-Insert-Objects-WithShape Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Insert_Objects_WithShape_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Which hole is for the cylinder?

**Options:**
A: A hole
B: B hole
C: C hole

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Insert_Objects_WithShape.png' alt='Tabletop-Insert-Objects-WithShape Query'>

### Tabletop-Merge-USB

**Environment ID:** `Tabletop-Merge-USB-v1`

**Instruction:** Pick up the USB body and insert it into the USB hub

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Merge_USB_v1_thumb_first.png' alt='Tabletop-Merge-USB Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Merge_USB_v1_thumb_last.png' alt='Tabletop-Merge-USB Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Merge_USB_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the correct orientation for inserting the USB?

**Options:**
A: Align the USB connector with the port and insert
B: Rotate the USB 180 degrees and insert with the port facing down

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Merge_USB.png' alt='Tabletop-Merge-USB Query'>

### Tabletop-Pick-Eraser-FromHolder

**Environment ID:** `Tabletop-Pick-Eraser-FromHolder-v1`

**Instruction:** Pick up the eraser in the holder and place it to the marker

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Eraser_FromHolder_v1_thumb_first.png' alt='Tabletop-Pick-Eraser-FromHolder Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Eraser_FromHolder_v1_thumb_last.png' alt='Tabletop-Pick-Eraser-FromHolder Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Pick_Eraser_FromHolder_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** How can we pick the eraser from the holder?

**Options:**
A: Pick the eraser directly
B: Pour out the rubber from the holder

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Pick_Eraser_FromHolder.png' alt='Tabletop-Pick-Eraser-FromHolder Query'>

### Tabletop-Move-Cube-DynamicFriction

**Environment ID:** `Tabletop-Move-Cube-DynamicFriction-v1`

**Instruction:** move the cube to the marker

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_DynamicFriction_v1_thumb_first.png' alt='Tabletop-Move-Cube-DynamicFriction Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_DynamicFriction_v1_thumb_last.png' alt='Tabletop-Move-Cube-DynamicFriction Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Move_Cube_DynamicFriction_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What's the best approach to move a cube with unpredictable friction?

**Options:**
A: Lift the cube and directly place it to the target position
B: Slide the cube while maintaining contact with the surface
C: Pick up blocks, re-pick them up if it falls

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Move_Cube_DynamicFriction.png' alt='Tabletop-Move-Cube-DynamicFriction Query'>

### Tabletop-Find-Cube-RedDown

**Environment ID:** `Tabletop-Find-Cube-RedDown-v1`

**Instruction:** find the cube which have red face downward, and put it on the marker with red face upward

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Cube_RedDown_v1_thumb_first.png' alt='Tabletop-Find-Cube-RedDown Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Cube_RedDown_v1_thumb_last.png' alt='Tabletop-Find-Cube-RedDown Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Cube_RedDown_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** which seal has red face downward

**Options:**
A: A
B: B
C: C

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Find_Cube_RedDown.png' alt='Tabletop-Find-Cube-RedDown Query'>

### Tabletop-Merge-Box

**Environment ID:** `Tabletop-Merge-Box-v1`

**Instruction:** Merge ball and boxs up

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Merge_Box_v1_thumb_first.png' alt='Tabletop-Merge-Box Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Merge_Box_v1_thumb_last.png' alt='Tabletop-Merge-Box Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Merge_Box_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** which box is to be inserted

**Options:**
A: Box A
B: Box B

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Merge_Box.png' alt='Tabletop-Merge-Box Query'>

### Tabletop-Open-Cabinet-WithDoor

**Environment ID:** `Tabletop-Open-Cabinet-WithDoor-v1`

**Instruction:** open the cabinet door

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithDoor_v1_thumb_first.png' alt='Tabletop-Open-Cabinet-WithDoor Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithDoor_v1_thumb_last.png' alt='Tabletop-Open-Cabinet-WithDoor Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithDoor_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What's the correct sequence of actions to open the cabinet?

**Options:**
A: Close the door first, then access the cabinet
B: Open the cabinet directly without interacting with the door

**Answer:** A
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Open_Cabinet_WithDoor.png' alt='Tabletop-Open-Cabinet-WithDoor Query'>

### Tabletop-Open-Cabinet-WithSwitch

**Environment ID:** `Tabletop-Open-Cabinet-WithSwitch-v1`

**Instruction:** open the door, notice the switch will control the state of the door

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithSwitch_v1_thumb_first.png' alt='Tabletop-Open-Cabinet-WithSwitch Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithSwitch_v1_thumb_last.png' alt='Tabletop-Open-Cabinet-WithSwitch Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Open_Cabinet_WithSwitch_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What is the efficient way to open the cabinet

**Options:**
A: Open the cabinet directly
B: Push the switch to open the cabinet

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Open_Cabinet_WithSwitch.png' alt='Tabletop-Open-Cabinet-WithSwitch Query'>

### Tabletop-Close-Drawer-WithObstacle

**Environment ID:** `Tabletop-Close-Drawer-WithObstacle-v1`

**Instruction:** close the drawer

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_WithObstacle_v1_thumb_first.png' alt='Tabletop-Close-Drawer-WithObstacle Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_WithObstacle_v1_thumb_last.png' alt='Tabletop-Close-Drawer-WithObstacle Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Close_Drawer_WithObstacle_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** What should do first before closing the drawer?

**Options:**
A: Open the cabinet
B: Move the stick away

**Answer:** B
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Close_Drawer_WithObstacle.png' alt='Tabletop-Close-Drawer-WithObstacle Query'>

### Tabletop-Find-Book-Black

**Environment ID:** `Tabletop-Find-Book-Black-v1`

**Instruction:** Find and pick the black book from the bookshelf and put it on the marker

**Initial State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Book_Black_v1_thumb_first.png' alt='Tabletop-Find-Book-Black Initial State'>

**Goal State:**
<img style='width:100%;max-width:400px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Book_Black_v1_thumb_last.png' alt='Tabletop-Find-Book-Black Goal State'>

**Video:**
<video width="400" controls>
  <source src="https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/medias/Tabletop_Find_Book_Black_v1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

**Query Text:** Where is the black book?

**Options:**
A: On the right column, the first book
B: In the middle column, the third book
C: On the left column, the second book

**Answer:** C
**Query Image:** <img style='max-width:300px;height:auto' src='https://raw.githubusercontent.com/Lr-2002/COIN_videos/main/interactive_task_image/Tabletop_Find_Book_Black.png' alt='Tabletop-Find-Book-Black Query'>
