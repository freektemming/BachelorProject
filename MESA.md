## Before start:

export MESASDK_ROOT=~/mesasdk
export MESA_DIR=~/mesa
source $MESASDK_ROOT/bin/mesasdk_init.sh

To close a file to which changes have been made (such as text having been added or removed) without saving the changes, hit ESC, type :q! and then press ENTER. This is sometimes referred to as a "forced quit."

vi works with a buffer (a block of memory in the RAM chips). When you open an existing file, vi copies that file from the hard disk (or floppy, CDROM, etc.) to a buffer. All changes that you make to a file are initially made only to the copy in the buffer, and they are only made to the file itself when you "save" your changes. "Saving" a file means writing (i.e., transferring) the contents of the buffer to the hard disk (or floppy disk).

Likewise when you open a new file. All text you enter (and subsequent edits you make to it) exists only in the buffer until you save the file to disk.

To save the changes that have been made to a file, hit ESC, type :qw and then press ENTER. The "w" stands for "write." An alternative, and perhaps easier, way to save a file and quit at the same time is to hit ESC and then type ZZ (two capital Z's in succession).

## Open file:

    cat filename

    xdg-open filename

    This works: vim filename
    and then: Once you opened a file with vim you can insert text by typing i, for instance. If you want to save your file use :w (write) or :q (quit) or :wq (for write and quit) or :q! (quit and do not save). Sometimes you need to hit the ESC key to be able to type the commands.

## copy star/work:

    cp -r $MESA_DIR/star/work tutorial

## to change column output:

    cp $MESA_DIR/star/defaults/history_columns.list .
    cp $MESA_DIR/star/defaults/profile_columns.list .

## run:

    ./rn