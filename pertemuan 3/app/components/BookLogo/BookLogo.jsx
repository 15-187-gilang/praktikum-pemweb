'use client';

const BookLogo = ({ size = 80 }) => {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 120 120"
      xmlns="http://www.w3.org/2000/svg"
      style={{ display: 'inline-block' }}
    >
      {/* Outer decorative circle border */}
      <circle cx="60" cy="60" r="55" fill="none" stroke="#D4AF6B" strokeWidth="3" />
      
      {/* Celtic pattern - top left */}
      <path
        d="M 25 30 Q 30 25 35 30 Q 30 35 25 30"
        fill="none"
        stroke="#D4AF6B"
        strokeWidth="2"
      />
      
      {/* Celtic pattern - top right */}
      <path
        d="M 95 30 Q 90 25 85 30 Q 90 35 95 30"
        fill="none"
        stroke="#D4AF6B"
        strokeWidth="2"
      />
      
      {/* Celtic pattern - bottom left */}
      <path
        d="M 25 90 Q 30 95 35 90 Q 30 85 25 90"
        fill="none"
        stroke="#D4AF6B"
        strokeWidth="2"
      />
      
      {/* Celtic pattern - bottom right */}
      <path
        d="M 95 90 Q 90 95 85 90 Q 90 85 95 90"
        fill="none"
        stroke="#D4AF6B"
        strokeWidth="2"
      />
      
      {/* Main book stack - green book (left) */}
      <rect x="32" y="45" width="18" height="22" fill="#2D8A4F" rx="2" />
      <rect x="32" y="45" width="18" height="3" fill="#1F5A36" />
      
      {/* Main book stack - blue book (middle) */}
      <rect x="52" y="38" width="18" height="30" fill="#1E3A8A" rx="2" />
      <rect x="52" y="38" width="18" height="3" fill="#0F1F4D" />
      
      {/* Main book stack - gold/tan book (right) */}
      <rect x="72" y="45" width="18" height="22" fill="#D4AF6B" rx="2" />
      <rect x="72" y="45" width="18" height="3" fill="#B8933D" />
      
      {/* Wing swoosh - left side (green) */}
      <path
        d="M 45 55 Q 40 50 35 55 Q 38 58 45 55"
        fill="#2D8A4F"
        opacity="0.8"
      />
      
      {/* Wing swoosh - middle (blue) */}
      <path
        d="M 50 48 Q 45 42 40 48 Q 45 52 50 48"
        fill="#1E3A8A"
        opacity="0.8"
      />
      
      {/* Wing swoosh - right (gold) */}
      <path
        d="M 75 55 Q 80 50 85 55 Q 82 58 75 55"
        fill="#D4AF6B"
        opacity="0.8"
      />
      
      {/* Center decorative circle */}
      <circle cx="60" cy="60" r="4" fill="#D4AF6B" />
    </svg>
  );
};

export default BookLogo;
