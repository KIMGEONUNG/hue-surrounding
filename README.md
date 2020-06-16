

## 1. Overview
- **Project Name : Hue-Surrounding**
- This project is for generating hue variation gif image. To get a quick intuition, see the images below .The input image was generated from [Sound Visualization Library](https://github.com/MYEONGJOONIL/Sound_Visualization) created by [MYEONGJOONIL](https://github.com/MYEONGJOONIL)



| <img src = "https://raw.githubusercontent.com/KIMGEONUNG/hue-surrounding/master/git_material/sample.png" width = "350">  | <img src = "https://raw.githubusercontent.com/KIMGEONUNG/hue-surrounding/master/git_material/result.gif" width = "350"> |
| :-------------: | :-------------: |
| **Input Image** | **Output gif** |
## 2. Dependency
- **Linux** : Ubuntu 18.04.4 LTS
- **Python** : ver. 3.6.9
- **PIL** : ver. 1.1.7
- **colorsys** 

## 3. Usage  

- **Execute Program**  
  ```Bash
  > python hue_surrounding.py -i ./sample_images/sample.png -o ./output.gif
  ```
- **Option Description**  
  ```Bash
  > python hue_surrounding.py -h
  -f : The number of frames 
  -i : Input image file path. Default path is "./sample_images/sample.png"
  -o : output image file path. Default path is "./output.gif"
  ```
  

## 4. Version
- Current up-to-date version : v1.0.0


