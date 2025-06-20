document.addEventListener('DOMContentLoaded', function() {
    // Add any interactive functionality here
    console.log('Weather app loaded');
    
    // Example: Focus on search input when page loads
    const searchInput = document.querySelector('input[name="city"]');
    if (searchInput) {
        searchInput.focus();
    }
    
    // You could add more interactive features like:
    // - Auto-complete for city names
    // - Geolocation to detect user's location
    // - Save favorite cities to localStorage
});