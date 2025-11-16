'use client';

import React from 'react';
import { useBookStats } from '../../lib/hooks/useBookStats';
import './Stats.css';

const Stats = ({ onNavigateHome }) => {
  const stats = useBookStats();

  const statItems = [
    { label: 'Total Buku', value: stats.total, emoji: '📚', color: '#667eea' },
    { label: 'Milik', value: stats.milik, emoji: '✅', color: '#10b981' },
    { label: 'Sedang Dibaca', value: stats.sedangDibaca, emoji: '📖', color: '#f59e0b' },
    { label: 'Ingin Dibeli', value: stats.inginDibeli, emoji: '🛒', color: '#3b82f6' },
  ];

  const getPercentage = (value) => {
    if (stats.total === 0) return 0;
    return Math.round((value / stats.total) * 100);
  };

  return (
    <div className="stats-page">
      <header className="stats-header">
        <button onClick={onNavigateHome} className="back-link">
          ← Kembali ke Home
        </button>
        <h1>📊 Statistik Perpustakaan</h1>
        <p>Ringkasan koleksi buku pribadi kamu</p>
      </header>

      <div className="stats-container">
        <div className="stats-grid">
          {statItems.map((item, index) => (
            <div 
              key={index} 
              className="stat-card"
              style={{ borderTopColor: item.color }}
            >
              <div className="stat-icon">{item.emoji}</div>
              <h3>{item.label}</h3>
              <p className="stat-value">{item.value}</p>
              <p className="stat-percentage">
                {getPercentage(item.value)}% dari total
              </p>
            </div>
          ))}
        </div>

        <div className="chart-section">
          <h2>📈 Distribusi Buku</h2>
          <div className="chart-bars">
            {statItems.slice(1).map((item, index) => (
              <div key={index} className="chart-bar-container">
                <div className="chart-label">
                  <span>{item.emoji} {item.label}</span>
                  <span className="chart-count">{item.value}</span>
                </div>
                <div className="chart-bar-bg">
                  <div 
                    className="chart-bar"
                    style={{
                      width: `${getPercentage(item.value)}%`,
                      backgroundColor: item.color
                    }}
                  />
                </div>
                <div className="chart-percentage">{getPercentage(item.value)}%</div>
              </div>
            ))}
          </div>
        </div>

        {stats.total === 0 && (
          <div className="empty-library">
            <p className="empty-icon">📚</p>
            <p>Belum ada data buku. Mulai tambah buku di halaman home!</p>
            <button onClick={onNavigateHome} className="btn-home">
              Tambah Buku Sekarang
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default Stats;
