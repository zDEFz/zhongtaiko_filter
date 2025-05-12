pkgname=zhongtaiko-filter
pkgver=1.0.0
pkgrel=1
pkgdesc="Filters ghost key events from ZhongTaiko [Pro] drum controllers using a root-run systemd service"
arch=('any')
url="https://github.com/zDEFz/zhongtaiko-filter"
license=('MIT')
depends=('python' 'python-evdev')

source=(
  "zhongtaiko_filter.py"
  "zhongtaiko-filter.service"
  "README.md"
  "LICENSE"
)
sha256sums=('SKIP' 'SKIP' 'SKIP' 'SKIP')

# Package the files into the proper locations
package() {
  # Install the Python script
  install -Dm755 "$srcdir/zhongtaiko_filter.py" \
    "$pkgdir/usr/lib/zhongtaiko-filter/zhongtaiko_filter.py"
  
  # Install the systemd service file
  install -Dm644 "$srcdir/zhongtaiko-filter.service" \
    "$pkgdir/etc/systemd/system/zhongtaiko_filter.service"

  # Optionally install documentation & license
  install -Dm644 "$srcdir/README.md" \
    "$pkgdir/usr/share/doc/${pkgname}/README.md"
  install -Dm644 "$srcdir/LICENSE" \
    "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}

# Include the post-install file for service management
install=zhongtaiko-filter.install
