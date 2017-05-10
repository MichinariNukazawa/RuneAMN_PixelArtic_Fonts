#
# License: BSD clause-2
# michinari.nukazawa@gmail.com
#

SOURCE_DIR	:= ./font_source
OBJECT_DIR	:= ./object
BUILD_DIR	:= ./build

SOURCE_IMAGES	:= $(wildcard $(SOURCE_DIR)/*.png)

TARGET_SVGS_b0	:= $(subst $(SOURCE_DIR),$(BUILD_DIR),$(SOURCE_IMAGES:.png=_b0.svg))
TARGET_LIST_TXTS_b0	:= $(TARGET_SVGS_b0:.svg=_list.txt)
TARGET_SVGS_b40	:= $(subst $(SOURCE_DIR),$(BUILD_DIR),$(SOURCE_IMAGES:.png=_b40.svg))
TARGET_LIST_TXTS_b40	:= $(TARGET_SVGS_b40:.svg=_list.txt)

TARGET_SVGS	:= $(TARGET_SVGS_b0) $(TARGET_SVGS_b40)
TARGET_LIST_TXTS	:= $(TARGET_LIST_TXTS_b0) $(TARGET_LIST_TXTS_b40)


.PHONY : fast
.PHONY : all clean
.PHONY : movefont

fast :
	echo $(TARGET_SVGS)
	make -j4 all

all : $(TARGET_SVGS) $(TARGET_LIST_TXTS)

$(OBJECT_DIR)/%_b40.png $(OBJECT_DIR)/%_b0.png : $(SOURCE_DIR)/%.png
	mkdir -p $(dir $@)
	cp $< $(@)

$(OBJECT_DIR)/%_list.txt : $(SOURCE_DIR)/%_list.txt
	mkdir -p $(dir $@)
	cp $< $(@)

$(TARGET_SVGS) : $(BUILD_DIR)/%.svg : $(OBJECT_DIR)/%.png $(OBJECT_DIR)/%_list.txt
	mkdir -p $(dir $@)
	python3 ./script/pixel_artic/image2svg.py $@ $<

$(TARGET_LIST_TXTS) : $(BUILD_DIR)/% : $(OBJECT_DIR)/%
	mkdir -p $(dir $@)
	cp $< $@

MOVE_DIST_DIR := ../../font_source
movefont: $(TARGET_SVGS) $(TARGET_LIST_TXTS)
	cp $^ $(MOVE_DIST_DIR)/

clean :
	rm -rf $(BUILD_DIR)/

