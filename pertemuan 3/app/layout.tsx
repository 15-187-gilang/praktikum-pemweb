import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Manajemen Buku Pribadi',
  description: 'Aplikasi React untuk mengelola koleksi buku pribadi',
    generator: 'v0.app'
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="id">
      <body>{children}</body>
    </html>
  );
}
