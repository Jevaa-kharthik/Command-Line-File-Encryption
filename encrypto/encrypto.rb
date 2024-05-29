class Encrypto < Formula
  include Language::Python::Virtualenv

  desc "Command Line File Encryption in Python"
  homepage "https://github.com/Jevaa-kharthik/Command-Line-File-Encryption"
  url "https://github.com/Jevaa-kharthik/Command-Line-File-Encryption/archive/v1.0.0.tar.gz"
  sha256 "your_tarball_checksum"
  license "MIT"

  depends_on "python"

  resource "cryptography" do
    url "https://files.pythonhosted.org/packages/3b/3c/3d3b1e82a76d26d5d1165b7fa4d8b5ebdfb2f4d6a1e0f7f54014f5bdf45b/cryptography-3.4.7.tar.gz"
    sha256 "abc123"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/encrypto", "--help"
  end
end

