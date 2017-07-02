#!/bin/sh
# add as many pyuic5 convertion that needed to create the project
#
cd $(dirname $0)

pyrcc5 ./gui/djtango.qrc -o djtango_rc.py &&\
#pyrcc5 ./gui/UI_askDelete.ui -o ./djtango/UI_askDelete.py &&\
pyuic5 ./gui/UI_djtango.ui -o ./djtango/UI_djtango.py &&\
pyuic5 ./gui/UI_details.ui -o ./djtango/UI_details.py &&\
pyuic5 ./gui/UI_infos.ui -o ./djtango/UI_infos.py &&\
pyuic5 ./gui/UI_preferences.ui -o ./djtango/UI_preferences.py &&\
pyuic5 ./gui/UI_milongaSelect.ui -o ./djtango/UI_selectmilonga.py &&\
pyuic5 ./gui/UI_milongaName.ui -o ./djtango/UI_milongaName.py &&\
pyuic5 ./gui/UI_sideDisplay.ui -o ./djtango/UI_sideDisplay.py &&\
pyuic5 ./gui/UI_tapbpm.ui -o ./djtango/UI_tapbpm.py &&\
pyuic5 ./gui/UI_infosMilonga.ui -o ./djtango/UI_infosMilonga.py &&\

pyuic5 ./gui/form.ui -o ./djtango/form.py &&\

./bin/DjtangoDialog.py