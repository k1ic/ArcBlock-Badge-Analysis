#!/usr/bin/sh
svg_file=$1
text_file=${svg_file/%rope/text}

if [ -f "$text_file" ]
then
	rm -rf $text_file
fi

#获取徽章标题
text_line_num=`grep -n '</text>' $svg_file | awk -F ':' '{ print $1}' | sort | tail -1`
text_line_num=`expr $text_line_num - 1`
get_text_cmd="sed -n '"$text_line_num",1p' "$svg_file
text=`echo $get_text_cmd | sh | sed 's/^[ \t]*//g'`

#统计徽章元素种类及数量
sun_total=`grep -c '<circle class="cls-sun' $svg_file`
moon_total=`grep -c 'class="cls-moon' $svg_file`
cloud_total=`grep -c 'class="cls-cloud' $svg_file`
bird_total=`grep -c 'class="cls-bird' $svg_file`
dog_total=`grep -c '<g id="dog"' $svg_file`
man_total=`grep -c '<g id="man"' $svg_file`
woman_total=`grep -c '<g id="woman"' $svg_file`
boy_total=`grep -c '<g id="boy"' $svg_file`

#单独统计羊的数量
sheep_total=`grep -c 'class="cls-many-sheep-2' $svg_file`
if [ $sheep_total -eq 0 ]
then
    sheep_total=`grep -c 'class="cls-less-sheep-2' $svg_file`
fi
if [ $sheep_total -eq 0 ]
then
    sheep_total=`grep -c 'id="Layer_12"' $svg_file`
fi

#单独统计兔子的数量
rabbit_total=`grep -c 'id="rabbit"' $svg_file`
if [ $rabbit_total -eq 0 ]
then
    rabbit_total=`grep -c 'id="rabbit_many"' $svg_file`
    if [ $rabbit_total -eq 1 ]
    then
        rabbit_total=2
    fi
fi
text_row="|$text|$sun_total|$moon_total|$cloud_total|$bird_total|$dog_total|$man_total|$woman_total|$boy_total|$sheep_total|$rabbit_total|"
echo $text_row
