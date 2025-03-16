// static/js/script.js
document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('search-form');
    const problemInput = document.getElementById('problem-input');
    const resultsContainer = document.getElementById('results-container');
    const loadingContainer = document.querySelector('.loading-container');

    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const problem = problemInput.value.trim();
        if (!problem) return;
        
        // Show loading spinner
        resultsContainer.innerHTML = '';
        loadingContainer.style.display = 'flex';
        
        try {
            // Create form data for the POST request
            const formData = new FormData();
            formData.append('problem', problem);
            
            // Send the search request
            const response = await fetch('/search', {
                method: 'POST',
                body: formData
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            // The data is already an array, no need to access .results
            displayResults(data);
        } catch (error) {
            console.error('Error:', error);
            displayError('An error occurred while searching. Please try again.');
        } finally {
            // Hide loading spinner
            loadingContainer.style.display = 'none';
        }
    });
    
    function displayResults(results) {
        resultsContainer.innerHTML = '';
        
        if (!results || results.length === 0) {
            resultsContainer.innerHTML = `
                <div class="no-results">
                    <i class="fa-solid fa-face-sad-tear"></i>
                    <p>No results found. Try a different math problem.</p>
                </div>
            `;
            return;
        }
        
        results.forEach(result => {
            const card = document.createElement('div');
            card.className = 'result-card';
            
            card.innerHTML = `
                <div class="card-content">
                    <h3 class="card-title">${escapeHTML(result.title)}</h3>
                    <a href="${escapeHTML(result.link)}" class="card-link" target="_blank">
                        View on Math StackExchange <i class="fa-solid fa-arrow-up-right-from-square"></i>
                    </a>
                </div>
            `;
            
            resultsContainer.appendChild(card);
        });
    }
    
    function displayError(message) {
        resultsContainer.innerHTML = `
            <div class="no-results" style="border-top: 4px solid var(--error-color);">
                <i class="fa-solid fa-circle-exclamation"></i>
                <p>${message}</p>
            </div>
        `;
    }
    
    // Helper function to prevent XSS
    function escapeHTML(str) {
        return str
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }
});
