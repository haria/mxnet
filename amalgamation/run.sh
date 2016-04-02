export USERSPACE=/opt/ndk/toolchain/arm_android19
export CXX=$USERSPACE/bin/arm-linux-androideabi-g++
export SYS_ROOT=$USERSPACE/sysroot
export INCLUDE=$USERSPACE/include/c++/4.9
make ANDROID=1
