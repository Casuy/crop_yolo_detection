#!/bin/bash

for FILE in /Users/zihany1/Documents/study/feral-cat-data/raw-dataset/otway_south/*; do
  echo "${FILE##*/}"
  image_dir="${FILE}/"
  label_dir="/Users/zihany1/Documents/study/projects/yolov5/runs/detect/${FILE##*/}/labels/"
  save_dir="/Users/zihany1/Documents/study/feral-cat-data/cropped/${FILE##*/}/"
  echo "image: ${image_dir}"
  echo "label: ${label_dir}"
  echo "save: ${save_dir}"
  if [[ ! -e /Users/zihany1/Documents/study/feral-cat-data/cropped/${FILE##*/} ]]; then
    mkdir -p /Users/zihany1/Documents/study/feral-cat-data/cropped/${FILE##*/}
  fi

  python main.py --image "${image_dir}" --label "${label_dir}" --save "${save_dir}"
  done