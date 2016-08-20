#!/bin/sh
# add as many pyuic4 convenstion that needed to create the project
#
pyuic4 ./gui/UI_djtango.ui -o ./djtango/UI_djtango.py &&\
pyuic4 ./gui/UI_details.ui -o ./djtango/UI_details.py &&\
pyuic4 ./gui/UI_infos.ui -o ./djtango/UI_infos.py &&\
pyuic4 ./gui/UI_preferences.ui -o ./djtango/UI_preferences.py &&\
pyuic4 ./gui/UI_milongaSelect.ui -o ./djtango/UI_selectmilonga.py &&\
pyuic4 ./gui/UI_milongaName.ui -o ./djtango/UI_milongaName.py &&\
pyuic4 ./gui/UI_sideDisplay.ui -o ./djtango/UI_sideDisplay.py &&\
pyuic4 ./gui/UI_tapbpm.ui -o ./djtango/UI_tapbpm.py &&\
pyuic4 ./gui/UI_infosMilonga.ui -o ./djtango/UI_infosMilonga.py &&\
pyuic4 ./gui/form.ui -o ./djtango/form.py &&\
pyrcc4 -py3 ./gui/djtango.qrc -o djtango_rc.py &&\

./bin/DjtangoDialog.py