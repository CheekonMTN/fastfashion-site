/**
 * Year Progress Calculator
 * Updates the CSS variable --water-progress based on how far through the year we are
 */

(function() {
    'use strict';

    function setYearProgress() {
        const now = new Date();
        
        // Start of this year (Jan 1, 00:00)
        const startOfYear = new Date(now.getFullYear(), 0, 1);
        
        // Start of next year (Jan 1 next year, 00:00)
        const startOfNextYear = new Date(now.getFullYear() + 1, 0, 1);
        
        const elapsedMs = now - startOfYear;
        const totalMs = startOfNextYear - startOfYear;
        
        let progress = (elapsedMs / totalMs) * 100;
        
        // Clamp to 0–100
        if (progress < 0) progress = 0;
        if (progress > 100) progress = 100;
        
        // Write into the CSS variable on :root (html element)
        document.documentElement.style.setProperty("--water-progress", progress);
    }
    
    // Run once when the page is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setYearProgress);
    } else {
        setYearProgress();
    }
    
    // Update periodically (every hour) to keep it accurate
    setInterval(setYearProgress, 3600000); // 3600000ms = 1 hour
})();

