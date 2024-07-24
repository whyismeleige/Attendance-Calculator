function weeksBetween(start_date, end_date) {
    const oneWeek = 1000 * 60 * 60 * 24 * 7;
    const delta = end_date - start_date;
    return Math.floor(delta / oneWeek);
}

function calculateAttendance() {
    const monday = parseInt(document.getElementById('monday').value);
    const tuesday = parseInt(document.getElementById('tuesday').value);
    const wednesday = parseInt(document.getElementById('wednesday').value);
    const thursday = parseInt(document.getElementById('thursday').value);
    const friday = parseInt(document.getElementById('friday').value);
    const saturday = parseInt(document.getElementById('saturday').value);

    let total;
    let avg;

    if (saturday === 0) {
        total = monday + tuesday + wednesday + thursday + friday;
        avg = total / 5;
    } else {
        total = monday + tuesday + wednesday + thursday + friday + saturday;
        avg = total / 6;
    }

    const joining_date = new Date(document.getElementById('joining_date').value);
    const end_date = new Date(document.getElementById('end_date').value);
    const current_date = new Date();

    const weeks_done = weeksBetween(joining_date, current_date);
    const weeks_left = weeksBetween(current_date, end_date);
    const today_total_classes = weeks_done * total;

    const current_attendance = parseInt(document.getElementById('current_attendance').value);
    const current_classes_attended = (current_attendance / 100) * today_total_classes;
    const cutoff_required = parseInt(document.getElementById('cutoff_required').value);

    const classes_left = weeks_left * total;
    const total_classes = today_total_classes + classes_left;
    const classes_cutoff = (cutoff_required / 100) * total_classes;
    const added_classes = current_classes_attended + classes_left;
    const max_attendance = (added_classes / total_classes) * 100;

    const resultElement = document.getElementById('result');

    if (added_classes > classes_cutoff) {
        const diff = added_classes - classes_cutoff;
        const holidays = Math.round(diff / avg);
        resultElement.innerHTML = `Number of holidays you can take: ${holidays}<br>Maximum Percentage Possible: ${max_attendance.toFixed(2)}%`;
    } else {
        resultElement.innerHTML = `Go to all classes<br>Maximum Percentage Possible:${max_attendance.toFixed(2)}%`;
    }
}
