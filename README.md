# 🦷 DentalStats | Brawl Stars 3D Edition

DentalStats is a gamified dentistry biostatistics learning platform designed to help students master statistical calculations and hypothesis testing through interactive, clinical-case scenarios wrapped in a vibrant **Brawl Stars 3D game theme**.

Access your calculations, check lookup tables, battle dentistry bosses, level up statistical brawlers, and test your skills in the Solo Showdown!

---

## 🎮 Game Features

### 1. 🏆 Trophy Road & Club Leaderboard
* **Trophy Progression**: Earn trophies by completing calculations (+50 🏆), matching variables (+20 🏆), defeating boss cases (+100 🏆), or winning quiz showdowns (+50 🏆).
* **Live Leaderboard**: Compete against standard bots (*Spike*, *Leon*, *Shelly*, *Colt*, *Poco*, and *Dental Bot*) to claim the Rank 1 Crown at **1,000 Trophies**!

### 2. 🤖 Statistical Brawler Library (Interactive 3D)
Unlock statistical heroes and rotate/interact with their **3D models** directly on their cards! Earn Power Points (PP) from calculations to level them up to **Power Level 5** to unlock exam tips and mastery secrets:
* **📊 Descriptive-Dynamo** (Tick) - Descriptive Stats & Outlier boundaries.
* **🔬 Variance-Viper** (Colette) - F-Test for Homogeneity of Variances.
* **⚖️ Mean-Machine** (Meg Mecha) - Independent Pooled t-Test.
* **🔄 Double-Impact** (Lunar Piper) - Paired sample t-Test (Repeated Measures).
* **📈 Matrix-Master** (DJ Frank) - Chi-Square Test of Independence.
* **🔔 Bell-Curve-Baron** (Spike) - Normal Distribution curve probability.

### 3. ⚔️ Boss Cases (3D Battles)
Dentistry bosses are attacking! Load datasets into the Arena to deal damage:
* **Situation 1 Boss: Hyper-Nitrate Behemoth** (Kaiju Boss) - 500 HP
* **Situation 2 Boss: Acid Saliva Dragon** (Rosales) - 500 HP
* **Situation 3 Boss: Endodontic Irrigator Golem** (Melee Bot) - 500 HP
* **Situation 4 Boss: Bell Curve Overlord** (Star Prize Boss) - 500 HP
* *Defeating a Boss rewards you with a **+100 🏆 Victory Bonus**!*

### 4. 🧠 Solo Showdown Quiz
* Fight through a **10-question interactive quiz** covering core biostatistics concepts (p-values, errors, F-distributions, Reciprocal Rule, etc.).
* Critical hits show step-by-step LaTeX formula explanations.

---

## ⚙️ How to Run Locally (Bypass CORS)

Because web browsers block loading local `3d Models/*.glb` assets via `file://` protocols for security (CORS), you must run a lightweight local HTTP server.

1. Install Python (if you haven't already).
2. Open the repository folder.
3. Double-click the server runner:
   ```bash
   python start_server.py
   ```
4. It will automatically host the platform and open your browser at **`http://localhost:8000`**.

---

## ☁️ How to Deploy to Render (Static Site)

To access your interactive study guide from any tablet or mobile device on the go, deploy it to Render:

1. Sign in to **[Render.com](https://render.com/)** using your GitHub account.
2. Click **New +** and select **Static Site**.
3. Connect the **`Dental-Stats`** repository.
4. Leave settings as default:
   * **Build Command**: *Blank/Empty*
   * **Publish Directory**: `.`
5. Click **Create Static Site**.

Render will deploy the site and provide a free, public URL (e.g., `https://dental-stats.onrender.com`).

---

## 📱 Mobile & iPad Support
The platform is fully responsive and supports mobile and iPad viewports:
* **Collapsible Sidebar**: Tap the **☰** icon in the header to toggle navigation options on small screens. Tap anywhere in the main content area to close the sidebar.
* **Scrollable Tables**: High-density lookup tables support horizontal scrolling/swiping so they do not break or overflow on small viewports.
* **Adaptive Grids**: Inputs and results stack vertically on smartphones, but sit side-by-side on tablet/desktop landscape viewports for optimal usability.
