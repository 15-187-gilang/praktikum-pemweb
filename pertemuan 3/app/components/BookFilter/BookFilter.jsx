'use client';

import React from 'react';
import './BookFilter.css';

const BookFilter = ({ onFilterChange }) => {
  const filters = ['Semua', 'Milik', 'Sedang Dibaca', 'Ingin Dibeli'];

  return (
    <div className="filter-container">
      <p className="filter-label">Filter Status:</p>
      <div className="filter-buttons">
        {filters.map(filter => (
          <button
            key={filter}
            onClick={() => onFilterChange(filter)}
            className="filter-btn"
          >
            {filter}
          </button>
        ))}
      </div>
    </div>
  );
};

export default BookFilter;
