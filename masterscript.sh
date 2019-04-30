#!/bin/bash
### call from python2.7 env
### using gnu-getopt (brew install gnu-getopt > then >   echo 'export PATH="/usr/local/opt/gnu-getopt/bin:$PATH"' >> ~/.bash_profile)
#detect if we have all arguments
# "-f" filename (mandatory)
    ## png (option)
# "-b" blender options
    ## geom "comma, seperated, list, of, geomfunctions(and their arguments)"
    ## render
        ### png
        ### svg
        ### fssvg (freestyle SVG)
# "-i" inkscape options (scour included)
    ## none (default)
    ## simplify
    ## scour (mandatory if other then none)
# "-c" chiplotle options 
    ## virtual / real
    ## layers
        ### hidden / unhidden
    ## scale (plotsize)
# "-g" git options
    ## if supplied commit with default message
    ## if supplied with argument include it in commit message

####https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
# saner programming env: these switches turn some bugs into errors
set -o errexit -o pipefail -o noclobber -o nounset

! getopt --test > /dev/null 
if [[ ${PIPESTATUS[0]} -ne 4 ]]; then
    echo 'I’m sorry, `getopt --test` failed in this environment.'
    exit 1
fi

OPTIONS=f:b:i::c:g::t::
LONGOPTS=file:,blender:,inkscape::,chiplotle:,git::,twitter::

! PARSED=$(getopt --options=$OPTIONS --longoptions=$LONGOPTS --name "$0" -- "$@")
if [[ ${PIPESTATUS[0]} -ne 0 ]]; then
    # e.g. return value is 1
    #  then getopt has complained about wrong arguments to stdout
    exit 2
fi
# read getopt’s output this way to handle the quoting right:
eval set -- "$PARSED"

echo "$PARSED"
f=nf b=nb c=nc ink=ni g=ng t=nt
# now enjoy the options in order and nicely split until we see --

while true; do
    case "$1" in
        -f|--file)
            echo "encounterd F $2"
            f="$2_$(date +"%m_%d_%Y_%H%M")"
            #var=$(expr $iter + $varoffset)
            echo $f
            shift 2
            ;;
        -b|--blender)
            echo "encounterd B $2"
            b="$2"
            shift 2
            ;;
        -i|--inkscape)
            echo "$1" "$2"
            echo "encounterd I $2"
            case "$2" in
                "") ink='some default value' ; shift 2 ;;
                *) ink=$2 ; shift 2 ;;
            esac ;;
        -c|--chiplotle)
            echo "encounterd C $2"
            c="$2"
            plot=1
            shift 2
            ;;
        -g|--git)
            echo "$1" "$2"
            echo "encounterd G $2"
            g=dogit
            case "$2" in
                "") gitmsg='default commit message, not feeling creative' ; shift 2 ;;
                *) gitmsg=$2 ; shift 2 ;;
            esac ;;
        -t|--twitter)
            echo "$1" "$2"
            echo "encounterd T $2"
            t=dotweet
            case "$2" in
                "") tweet='default tweetmessage, not feeling creative, look at the picture' ; shift 2 ;;
                *) tweet=$2 ; shift 2 ;;
            esac ;;
        --)
            shift
            break
            ;;
        *)
            echo "Programming error"
            exit 3
            ;;
    esac
    #iter=$(expr $iter + 1)
done

#handle non-option arguments
if [[ $f == nf ]]; then
    echo "output filename is required. set it using -f and do it like -fMyFile and not -f MyFile"
    exit 4
fi



echo "filename: $f, blenderopts: $b, inkscpaeopts: $ink, chiplotleopts: $c"

###calling BLENDER 
/Applications/Blender/blender.app/Contents/MacOS/blender stroketesting.blend --background --python generateandrender.py -- $b -f $f

pngname=$f.png
svgfilename=$f
svgfilename+=0000.svg 

#### calling inkscape
if [ $ink != ni ]; then
    cp $PWD/$filename $PWD/processed_$filename
    /usr/local/bin/inkscape $PWD/processed_$filename --verb EditSelectAll --verb SelectionSimplify --verb FileSave --verb FileQuit
    # python plotrender.py $PWD/processed_$filename $3 $5
fi

#### calling chiplotle
if [ $plot == 1 ]; then
    python plotrender.py $PWD/$svgfilename $c
fi

##call git
if [ $g == dogit ]; then
    git add $svgfilename
    git commit -a -m "plotting $g"
fi

##post to twitter?
if [ $t != nt ]; then
    python tweetplot.py "$tweet" $pngname
fi