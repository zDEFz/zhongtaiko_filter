pkgname=zhongtaiko_filter_py
pkgver=1.0.0
pkgrel=1
pkgdesc="Filters ghost key events from ZhongTaiko [Pro] drum controllers using a root-run systemd service"
arch=('any')
url="https://github.com/zDEFz/${pkgname}"
license=('MIT')
depends=('python' 'python-evdev')

# Clone the GitHub repository
source=("git+https://github.com/zDEFz/${pkgname}.git#commit=main")

# No need for sha256sums when using git clone
sha256sums=('SKIP')

# Package the files into the proper locations
package() {
  # Change directory to the cloned repository (it will be named ${pkgname})
  cd "$srcdir/${pkgname}"

  # Install the Python script
  install -Dm755 "$srcdir/${pkgname}.py" \
    "$pkgdir/usr/lib/${pkgname}/${pkgname}.py"
  
  # Install the systemd service file
  install -Dm644 "$srcdir/${pkgname}.service" \
    "$pkgdir/etc/systemd/system/${pkgname}.service"

  # Optionally install documentation & license
  install -Dm644 "$srcdir/README.md" \
    "$pkgdir/usr/share/doc/${pkgname}/README.md"
  install -Dm644 "$srcdir/LICENSE" \
    "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}

