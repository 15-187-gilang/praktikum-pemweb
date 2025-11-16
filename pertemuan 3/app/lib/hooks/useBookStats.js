import { useContext } from 'react';
import { BookContext } from '../context/BookContext';

export const useBookStats = () => {
  const { books } = useContext(BookContext);

  const stats = {
    total: books.length,
    milik: books.filter(b => b.status === 'Milik').length,
    sedangDibaca: books.filter(b => b.status === 'Sedang Dibaca').length,
    inginDibeli: books.filter(b => b.status === 'Ingin Dibeli').length,
  };

  return stats;
};
