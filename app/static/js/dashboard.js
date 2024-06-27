document.addEventListener('DOMContentLoaded', function() {
    // Fetch team stats and create chart
    fetch('/api/team_stats')
        .then(response => response.json())
        .then(data => {
            const ctx = document.getElementById('teamPointsChart').getContext('2d');
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.map(team => team.name),
                    datasets: [{
                        label: 'Points',
                        data: data.map(team => team.points),
                        backgroundColor: 'rgba(75, 192, 192, 0.6)'
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });

    // Fetch recent matches and populate list
    fetch('/api/recent_matches')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('recentMatchesList');
            data.forEach(match => {
                const li = document.createElement('li');
                li.textContent = `${match.home} ${match.score} ${match.away}`;
                list.appendChild(li);
            });
        });
});