import re

for filepath in ["tools-phones.html", "tools-compare.html"]:
    with open(filepath, "r") as f:
        content = f.read()

    # Find the load event listener to inject about.json fetching
    old_load = 'window.addEventListener("load", async function(){'
    
    # We'll replace it with a version that fetches about.json first and updates the header
    new_load = '''window.addEventListener("load", async function(){
        // Fetch and update profile info dynamically from about.json
        try {
            const aboutRes = await fetch('content/data/about.json');
            if (aboutRes.ok) {
                const aboutData = await aboutRes.json();
                const profileImgEl = document.getElementById('header-profile-img');
                const profileNameEl = document.getElementById('header-profile-name');
                if (profileImgEl && aboutData.profileImage) {
                    profileImgEl.src = aboutData.profileImage;
                }
                if (profileNameEl && aboutData.name) {
                    profileNameEl.textContent = aboutData.name;
                }
            }
        } catch(e) {
            console.error('Failed to load about data:', e);
        }
'''
    if old_load in content:
        content = content.replace(old_load, new_load)
        with open(filepath, "w") as f:
            f.write(content)
        print(f"Updated profile fetching in {filepath}")
    else:
        # Check if the function signature is different
        old_load_sync = 'window.addEventListener("load", function(){'
        if old_load_sync in content:
            new_load_async = '''window.addEventListener("load", async function(){
        // Fetch and update profile info dynamically from about.json
        try {
            const aboutRes = await fetch('content/data/about.json');
            if (aboutRes.ok) {
                const aboutData = await aboutRes.json();
                const profileImgEl = document.getElementById('header-profile-img');
                const profileNameEl = document.getElementById('header-profile-name');
                if (profileImgEl && aboutData.profileImage) {
                    profileImgEl.src = aboutData.profileImage;
                }
                if (profileNameEl && aboutData.name) {
                    profileNameEl.textContent = aboutData.name;
                }
            }
        } catch(e) {
            console.error('Failed to load about data:', e);
        }
'''
            content = content.replace(old_load_sync, new_load_async)
            with open(filepath, "w") as f:
                f.write(content)
            print(f"Updated profile fetching (changed to async) in {filepath}")
        else:
            print(f"Could not find window.addEventListener('load') in {filepath}")

