git pull 
git pull upstream
git merge upstream/master
git submodule foreach git submodule update
git push
cd dmlc-core
git checkout HEAD
cd -
cd mshadow
git checkout HEAD
cd -
cd ps-lite
git checkout HEAD
cd -
