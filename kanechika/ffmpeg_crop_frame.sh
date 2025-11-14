#!/bin/bash
# 指定したフレームおよび領域を静止画(png)として切り出す
FFMPEG=/mnt/c/opt/ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe

# ifpath=../2025_0807_sozai-noaudio.mp4
# fname=umaoi_drone1_2
# fname=prtg_0607_1_1011_1027_176_180_fps2_output
fname=kanechika
odir=./$fname
ifpath=./$fname.wmv

echo "Making directory: $odir"
mkdir -p $odir

# 先にKdenlive でフレームを切り出して位置を確認

# list of input frame numbers (checked on Kdenlive)

# # for [umaoi_drone1_2]
# frame_list="10000 11000 12000 13000"
# # crop area
# x=1264
# y=680
# w=1600
# h=1200

# # for [prtg_0607_1_1011_1027_176_180_fps2_output]
# frame_list="1100 1110 1120 1130"
# # crop area
# x=756
# y=628
# w=1600
# h=1200

# for [prtg_0610_1_1116_1128_182_186]
frame_list="300 305 310 315 320 325 330 335 340 345 350"
# crop area
x=132
y=256
w=1080
h=256



# frame_list=(1500 1600 1700 1800)
# select_filter=$(printf "eq(n\\,%s)+" "${frame_list[@]}")
# select_filter=${filter%+}  # 最後の + を削除

# generate select=eq filter for each frame
count=0
select_filter="select='"
for frame in $frame_list; do
  select_filter="${select_filter}eq(n\,$frame)+"
  count=$((count + 1))
done
# remove the last '+' and close the filter
select_filter="${select_filter%+}'"


echo "Using select filter: $select_filter"
# extract the frames and crop the area as PNG images
$FFMPEG -i $ifpath -vf "$select_filter,crop=$w:$h:$x:$y" -vsync passthrough -frames:v $count -frame_pts true $odir/frame_%04d.png
echo "Extracted frames and cropped area to PNG images."

# for each frame in the list
# for frame in $frame_list; do
#   # extract the frame and crop the area as a PNG image
# #   $FFMPEG -i $ifpath -vf "select=eq(n\,$frame),crop=$w:$h:$x:$y" -frame_pts 1 -vsync 0 frame_$frame.png
#   $FFMPEG -i $ifpath -vf "select=eq(n\,$frame)" -vframes 1 frame_$frame.png
#   echo "Extracted frame $frame and cropped area to frame_$frame.png"
# done  
