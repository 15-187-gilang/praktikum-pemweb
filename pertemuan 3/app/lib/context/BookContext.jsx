'use client';

import React, { createContext, useState, useCallback } from 'react';
import { useLocalStorage } from '../hooks/useLocalStorage';

export const BookContext = createContext();

export const BookProvider = ({ children }) => {
  const [books, setBooks] = useLocalStorage('books', []);

  const addBook = useCallback((book) => {
    const newBook = {
      id: Date.now(),
      ...book,
      createdAt: new Date().toISOString(),
    };
    setBooks([...books, newBook]);
    return newBook;
  }, [books, setBooks]);

  const updateBook = useCallback((id, updatedBook) => {
    setBooks(books.map(book => 
      book.id === id ? { ...book, ...updatedBook } : book
    ));
  }, [books, setBooks]);

  const deleteBook = useCallback((id) => {
    setBooks(books.filter(book => book.id !== id));
  }, [books, setBooks]);

  const value = {
    books,
    addBook,
    updateBook,
    deleteBook,
  };

  return (
    <BookContext.Provider value={value}>
      {children}
    </BookContext.Provider>
  );
};
