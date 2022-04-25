#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-utf8
Version  : 1.2.2
Release  : 42
URL      : https://cran.r-project.org/src/contrib/utf8_1.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/utf8_1.2.2.tar.gz
Summary  : Unicode Text Processing
Group    : Development/Tools
License  : Apache-2.0 ICU
Requires: R-utf8-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
text (Unicode). Input, validate, normalize, encode, format, and
    display.

%package lib
Summary: lib components for the R-utf8 package.
Group: Libraries

%description lib
lib components for the R-utf8 package.


%prep
%setup -q -c -n utf8
cd %{_builddir}/utf8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641143456

%install
export SOURCE_DATE_EPOCH=1641143456
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library utf8
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library utf8
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library utf8
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc utf8 || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/utf8/DESCRIPTION
/usr/lib64/R/library/utf8/INDEX
/usr/lib64/R/library/utf8/LICENSE
/usr/lib64/R/library/utf8/Meta/Rd.rds
/usr/lib64/R/library/utf8/Meta/features.rds
/usr/lib64/R/library/utf8/Meta/hsearch.rds
/usr/lib64/R/library/utf8/Meta/links.rds
/usr/lib64/R/library/utf8/Meta/nsInfo.rds
/usr/lib64/R/library/utf8/Meta/package.rds
/usr/lib64/R/library/utf8/Meta/vignette.rds
/usr/lib64/R/library/utf8/NAMESPACE
/usr/lib64/R/library/utf8/R/utf8
/usr/lib64/R/library/utf8/R/utf8.rdb
/usr/lib64/R/library/utf8/R/utf8.rdx
/usr/lib64/R/library/utf8/doc/index.html
/usr/lib64/R/library/utf8/doc/utf8.Rmd
/usr/lib64/R/library/utf8/doc/utf8.html
/usr/lib64/R/library/utf8/help/AnIndex
/usr/lib64/R/library/utf8/help/aliases.rds
/usr/lib64/R/library/utf8/help/paths.rds
/usr/lib64/R/library/utf8/help/utf8.rdb
/usr/lib64/R/library/utf8/help/utf8.rdx
/usr/lib64/R/library/utf8/html/00Index.html
/usr/lib64/R/library/utf8/html/R.css
/usr/lib64/R/library/utf8/tests/testthat.R
/usr/lib64/R/library/utf8/tests/testthat/_snaps/utf8_format.md
/usr/lib64/R/library/utf8/tests/testthat/helper-capture_output.R
/usr/lib64/R/library/utf8/tests/testthat/helper-locale.R
/usr/lib64/R/library/utf8/tests/testthat/helper-options.R
/usr/lib64/R/library/utf8/tests/testthat/helper-output.R
/usr/lib64/R/library/utf8/tests/testthat/setup.R
/usr/lib64/R/library/utf8/tests/testthat/test-utf8_encode.R
/usr/lib64/R/library/utf8/tests/testthat/test-utf8_format.R
/usr/lib64/R/library/utf8/tests/testthat/test-utf8_normalize.R
/usr/lib64/R/library/utf8/tests/testthat/test-utf8_print.R
/usr/lib64/R/library/utf8/tests/testthat/test-utf8_valid.R
/usr/lib64/R/library/utf8/tests/testthat/test-utf8_width.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/utf8/libs/utf8.so
/usr/lib64/R/library/utf8/libs/utf8.so.avx2
/usr/lib64/R/library/utf8/libs/utf8.so.avx512
