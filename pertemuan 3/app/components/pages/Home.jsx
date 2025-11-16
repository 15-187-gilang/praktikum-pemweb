'use client';

import React, { useState, useContext } from 'react';
import { BookContext } from '../../lib/context/BookContext';
import BookForm from '../BookForm/BookForm';
import BookFilter from '../BookFilter/BookFilter';
import SearchBar from '../SearchBar/SearchBar';
import BookList from '../BookList/BookList';
import BookLogo from '../BookLogo/BookLogo';
import './Home.css';

const Home = ({ onNavigateToStats }) => {
  const { books, deleteBook } = useContext(BookContext);
  const [filteredBooks, setFilteredBooks] = useState(books);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedFilter, setSelectedFilter] = useState('Semua');
  const [editingBook, setEditingBook] = useState(null);

  const applyFilters = (query = searchQuery, filter = selectedFilter) => {
    let result = books;

    if (filter !== 'Semua') {
      result = result.filter(book => book.status === filter);
    }

    if (query.trim()) {
      result = result.filter(book =>
        book.title.toLowerCase().includes(query.toLowerCase()) ||
        book.author.toLowerCase().includes(query.toLowerCase())
      );
    }

    setFilteredBooks(result);
  };

  const handleFilterChange = (filter) => {
    setSelectedFilter(filter);
    applyFilters(searchQuery, filter);
  };

  const handleSearch = (query) => {
    setSearchQuery(query);
    applyFilters(query, selectedFilter);
  };

  const handleDelete = (id) => {
    if (window.confirm('Apakah kamu yakin ingin menghapus buku ini?')) {
      deleteBook(id);
    }
  };

  const handleEdit = (book) => {
    setEditingBook(book);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleCancelEdit = () => {
    setEditingBook(null);
  };

  const handleBookAdded = () => {
    setEditingBook(null);
    applyFilters(searchQuery, selectedFilter);
  };

  return (
    <div className="home-page">
      <header className="home-header">
        <div className="header-content">
          <div className="logo-container">
            <BookLogo size={100} />
          </div>
          <h1>My Book Library</h1>
          <p>Kelola koleksi buku pribadi kamu dengan mudah</p>
          <button onClick={onNavigateToStats} className="stats-link">
            📊 Lihat Statistik
          </button>
        </div>
      </header>

      <div className="container">
        <div className="form-section">
          <BookForm 
            onBookAdded={handleBookAdded}
            editingBook={editingBook}
            onCancelEdit={handleCancelEdit}
          />
        </div>

        <div className="content-section">
          <SearchBar onSearch={handleSearch} />
          <BookFilter onFilterChange={handleFilterChange} />
          <BookList 
            books={filteredBooks} 
            onDelete={handleDelete}
            onEdit={handleEdit}
          />
        </div>
      </div>
    </div>
  );
};

export default Home;
