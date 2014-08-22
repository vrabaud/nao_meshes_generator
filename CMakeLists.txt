cmake_minimum_required(VERSION 2.8)
project(nao_meshes)

find_package(catkin)
catkin_package()

set(TMP_DIR_LOCAL ${CATKIN_DEVEL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}/tmp)
set(TMP_DIR ${CATKIN_DEVEL_PREFIX}/${CATKIN_GLOBAL_SHARE_DESTINATION}/../tmp)

set(INSTALLER_TMP_PATH ${TMP_DIR_LOCAL}/installer.run)

file(DOWNLOAD "https://github.com/vrabaud/nao_meshes_generator/raw/master/binaries/naomeshes-0.6.3-linux-x64-installer.run"
     ${INSTALLER_TMP_PATH} SHOW_PROGRESS
)

file(COPY ${INSTALLER_TMP_PATH}
     FILE_PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE
     DESTINATION ${TMP_DIR}
)

# unzip
set(INSTALLER_PATH ${TMP_DIR}/installer.run)
message(INFO "${INSTALLER_PATH} --mode unattended --prefix ${CATKIN_DEVEL_PREFIX}/${CATKIN_PACKAGE_SHARE_DESTINATION}")
#execute_process(COMMAND ${INSTALLER_PATH} --mode unattended --prefix ${TMP_DIR}
#                OUTPUT_VARIABLE OUT
#                ERROR_VARIABLE ERROR
#                RESULT_VARIABLE RESULT
#)
message(INFO ${OUT})
message(INFO ${ERROR})
message(INFO ${RESULT})

# install
message(INFO ${CATKIN_PACKAGE_SHARE_DESTINATION}/../)
install(DIRECTORY ${TMP_DIR}/nao_meshes/meshes/
        DESTINATION ${CATKIN_GLOBAL_SHARE_DESTINATION}/nao_description/meshes/
)
