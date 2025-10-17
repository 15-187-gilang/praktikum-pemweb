// Global array untuk menyimpan semua tugas
let arrayTasks = [];

// Fungsi untuk menyimpan data ke localStorage
const saveTasks = () => {
    // Sesuai petunjuk: Gunakan localStorage.setItem('tasks', JSON.stringify(arrayTasks))
    localStorage.setItem('tasks', JSON.stringify(arrayTasks));
    updatePendingCount(); // Perbarui statistik setelah menyimpan
};

// Fungsi untuk memuat data dari localStorage
const loadTasks = () => {
    // Sesuai petunjuk: Gunakan JSON.parse(localStorage.getItem('tasks'))
    const storedTasks = localStorage.getItem('tasks');
    if (storedTasks) {
        arrayTasks = JSON.parse(storedTasks);
    }
    renderTasks(); // Tampilkan tugas yang dimuat
};

// Fungsi untuk menampilkan tugas ke UI berdasarkan filter
const renderTasks = () => {
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = ''; // Kosongkan daftar saat ini

    const filterStatus = document.getElementById('filter-status').value;
    const filterCourse = document.getElementById('filter-course').value.toLowerCase();

    const filteredTasks = arrayTasks.filter(task => {
        // Filter berdasarkan Status
        const statusMatch = (filterStatus === 'all') ||
                            (filterStatus === 'pending' && !task.isCompleted) ||
                            (filterStatus === 'completed' && task.isCompleted);

        // Filter berdasarkan Mata Kuliah (Pencarian)
        const courseMatch = task.course.toLowerCase().includes(filterCourse);

        return statusMatch && courseMatch;
    });

    // Tampilkan tugas yang difilter
    filteredTasks.forEach((task, index) => {
        const listItem = document.createElement('li');
        listItem.classList.add('task-item');
        if (task.isCompleted) {
            listItem.classList.add('completed');
        }
        
        // Cari index asli dari tugas di arrayTasks (penting untuk fungsi delete/complete)
        const originalIndex = arrayTasks.findIndex(t => t.id === task.id);

        listItem.innerHTML = `
            <div class="task-details">
                <h4>${task.name}</h4>
                <p>Mata Kuliah: ${task.course}</p>
                <p>Deadline: ${task.deadline}</p>
                <p>Status: <strong>${task.isCompleted ? 'Selesai' : 'Belum Selesai'}</strong></p>
            </div>
            <div class="task-actions">
                <button class="complete-btn" data-index="${originalIndex}">
                    ${task.isCompleted ? 'Batal Selesai' : 'Tandai Selesai'}
                </button>
                <button class="delete-btn" data-index="${originalIndex}">Hapus</button>
            </div>
        `;

        taskList.appendChild(listItem);
    });

    updatePendingCount();
};

// Fungsi untuk validasi form
const validateForm = (taskName, courseName, deadline) => {
    // Validasi Tugas tidak boleh kosong
    if (!taskName.trim() || !courseName.trim() || !deadline.trim()) {
        alert("Validasi Form Gagal: Nama Tugas, Mata Kuliah, dan Deadline tidak boleh kosong!");
        return false;
    }

    // Validasi Deadline harus valid (tidak di masa lalu)
    const today = new Date();
    today.setHours(0, 0, 0, 0); // Atur waktu ke 00:00:00 untuk perbandingan tanggal saja
    const deadlineDate = new Date(deadline);
    
    // Memberi toleransi satu hari, agar hari H masih bisa diinput
    if (deadlineDate < today && deadlineDate.toDateString() !== today.toDateString()) {
        alert("Validasi Form Gagal: Deadline tidak boleh sudah terlewati!");
        return false;
    }

    return true;
};

// Handler untuk form submission (Menambah Tugas Baru)
document.getElementById('task-form').addEventListener('submit', (e) => {
    e.preventDefault();
    
    const taskNameInput = document.getElementById('taskName');
    const courseNameInput = document.getElementById('courseName');
    const deadlineInput = document.getElementById('deadline');

    const taskName = taskNameInput.value;
    const courseName = courseNameInput.value;
    const deadline = deadlineInput.value;

    // Lakukan Validasi
    if (!validateForm(taskName, courseName, deadline)) {
        return; // Hentikan jika validasi gagal
    }

    // Buat objek tugas baru
    const newTask = {
        id: Date.now(), // ID unik berdasarkan timestamp
        name: taskName,
        course: courseName,
        deadline: deadline,
        isCompleted: false
    };

    // Tambahkan tugas ke array dan simpan ke localStorage
    arrayTasks.push(newTask);
    saveTasks();

    // Reset form dan render ulang daftar
    taskNameInput.value = '';
    courseNameInput.value = '';
    deadlineInput.value = '';
    renderTasks();
});

// Handler untuk Aksi (Tandai Selesai dan Hapus)
document.getElementById('task-list').addEventListener('click', (e) => {
    const target = e.target;
    const index = target.dataset.index;

    if (index === undefined) return;

    // Aksi Tandai Selesai / Batal Selesai
    if (target.classList.contains('complete-btn')) {
        arrayTasks[index].isCompleted = !arrayTasks[index].isCompleted; // Toggle status
        saveTasks();
        renderTasks();
    }
    
    // Aksi Hapus
    if (target.classList.contains('delete-btn')) {
        if (confirm(`Yakin ingin menghapus tugas: "${arrayTasks[index].name}"?`)) {
            arrayTasks.splice(index, 1); // Hapus 1 elemen dari array pada index tersebut
            saveTasks();
            renderTasks();
        }
    }
});

// Handler untuk Filter dan Pencarian
document.getElementById('filter-status').addEventListener('change', renderTasks);
document.getElementById('filter-course').addEventListener('input', renderTasks); // Event 'input' untuk pencarian real-time

// Fungsi untuk menampilkan jumlah tugas yang belum selesai
const updatePendingCount = () => {
    const pendingCount = arrayTasks.filter(task => !task.isCompleted).length;
    document.getElementById('pending-count').textContent = pendingCount;
};

// Memuat data saat halaman pertama kali dibuka
window.onload = loadTasks;