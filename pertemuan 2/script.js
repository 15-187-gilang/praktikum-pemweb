// === CLASS UNTUK MENGELOLA JADWAL ===
class ScheduleManager {
  constructor() {
    this.schedules = JSON.parse(localStorage.getItem('schedules')) || [];
  }

  addSchedule(schedule) {
    this.schedules.push(schedule);
    this.save();
  }

  editSchedule(index, newSchedule) {
    this.schedules[index] = newSchedule;
    this.save();
  }

  deleteSchedule(index) {
    this.schedules.splice(index, 1);
    this.save();
  }

  save() {
    localStorage.setItem('schedules', JSON.stringify(this.schedules));
  }
}

// === INISIALISASI OBJEK DAN ELEMEN ===
const scheduleManager = new ScheduleManager();
const matkulInput = document.getElementById('matkulInput');
const hariInput = document.getElementById('hariInput');
const jamInput = document.getElementById('jamInput');
const addScheduleBtn = document.getElementById('addScheduleBtn');
const tableBody = document.querySelector('#scheduleTable tbody');
const currentTime = document.getElementById('currentTime');

// === FUNGSI UNTUK RENDER JADWAL (ARROW + TEMPLATE LITERALS) ===
const renderSchedules = () => {
  tableBody.innerHTML = scheduleManager.schedules.map((s, i) => `
    <tr>
      <td>${s.matkul}</td>
      <td>${s.hari}</td>
      <td>${s.jam}</td>
      <td>
        <button onclick="editSchedule(${i})">✏️</button>
        <button onclick="deleteSchedule(${i})">❌</button>
      </td>
    </tr>
  `).join('');
};

// === TAMBAH DATA (ARROW FUNCTION) ===
addScheduleBtn.addEventListener('click', () => {
  const matkul = matkulInput.value.trim();
  const hari = hariInput.value.trim();
  const jam = jamInput.value.trim();

  if (matkul && hari && jam) {
    scheduleManager.addSchedule({ matkul, hari, jam });
    matkulInput.value = hariInput.value = jamInput.value = '';
    renderSchedules();
  } else {
    alert("Lengkapi semua kolom jadwal!");
  }
});

// === EDIT DAN DELETE DATA ===
const editSchedule = (index) => {
  const jadwal = scheduleManager.schedules[index];
  const newMatkul = prompt("Edit nama matkul:", jadwal.matkul);
  const newHari = prompt("Edit hari:", jadwal.hari);
  const newJam = prompt("Edit jam:", jadwal.jam);

  if (newMatkul && newHari && newJam) {
    scheduleManager.editSchedule(index, { matkul: newMatkul, hari: newHari, jam: newJam });
    renderSchedules();
  }
};

const deleteSchedule = (index) => {
  if (confirm("Yakin ingin menghapus jadwal ini?")) {
    scheduleManager.deleteSchedule(index);
    renderSchedules();
  }
};

// === ASYNC/AWAIT UNTUK JAM REAL-TIME (SIMULASI DATA ASINKRON) ===
const updateTime = async () => {
  while (true) {
    await new Promise(resolve => setTimeout(resolve, 1000)); // delay 1 detik
    const now = new Date();
    const timeStr = now.toLocaleTimeString('id-ID', { hour12: false });
    currentTime.textContent = timeStr;
  }
};

// === INISIALISASI ===
renderSchedules();
updateTime();
