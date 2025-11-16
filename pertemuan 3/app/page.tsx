'use client';

import React, { useState } from 'react';
import { BookProvider } from './lib/context/BookContext';
import Home from './components/pages/Home';
import Stats from './components/pages/Stats';

export default function Page() {
  const [currentPage, setCurrentPage] = useState('home');

  return (
    <BookProvider>
      <div className="app-container">
        {currentPage === 'home' && (
          <Home onNavigateToStats={() => setCurrentPage('stats')} />
        )}
        {currentPage === 'stats' && (
          <Stats onNavigateHome={() => setCurrentPage('home')} />
        )}
      </div>
    </BookProvider>
  );
}
