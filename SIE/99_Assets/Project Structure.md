


Notes:

- Create a "Document Tree / Registry / Database" for internal structure.
- Create a document outlining external structure:
	- Core local copy with vault or backup or Google Drive cloud solution. 
		- Top Level Admin
	- Human Oversight at GitHub repository. Backup and version control.
		- Human Stewards
	- Sync's to website
	- Emedding in vector database.

---

# Document Database

### Structure:

Here’s how we can apply this "structured simplicity" to your proposed hierarchy. This becomes the blueprint for the **Master Hub**.


#### `/engine/`

_This folder describes the Strategic Intelligence Engine itself—its purpose, rules, and logs._

- `00_engine-overview.md` (Replaces `engine.md` - What is the engine's purpose?)
- `01_governance-rules.md` (Defines the operational rules for the engine)
- `02_interaction-logs.md` (A place for the engine to record significant actions)

#### `/strategy/`

_The "why" and "how" of the business's go-to-market plan._

- `00_core-vision-and-mission.md` (The highest-level strategy doc)
- `01_icp-and-personas.md` (Defines the Ideal Customer Profile)
- `02_go-to-market-plan.md`
- `s_seo-strategy.md` (The 's' prefix could mean 'sub-strategy' or 'specialized')
- `s_social-media-strategy.md`

#### `/intelligence/`

_The raw data the engine learns from—the "who" and "what" of the market._

- `c_competitor-analysis.md` (The 'c' prefix could mean 'competitive')
- `m_market-trends.md` (The 'm' prefix could mean 'market')
- `f_client-feedback-summary.md` (The 'f' prefix could mean 'feedback')

#### `/products/` (or `/offerings/`)

_The canonical descriptions of what the business sells._

- `p_core-offering-a.md`
- `p_service-package-b.md`
- `pricing-sheet.md`

---

## Archive

This guide outlines a comprehensive structure for managing the entire WPJet.ai business and its client projects within Obsidian. The system is designed around two core vaults to ensure a clean separation between your internal operations and the client deliverables.

1. **WPJet.ai Business Vault:** The central hub for all company strategy, client management, marketing, and product development.
    
2. **Client Blueprint Template Vault:** A clean, reusable template that is duplicated for each new client to create their Marketing Blueprint.
## 1. The Business Vault Structure

This is your main, private vault for running the business.

```
Business Vault/
├── 00_Dashboard.md
├── 01_Strategy/
│   ├── 1.0_Strategic_Engine.md
│   └── MOC_Strategy.md
├── 02_Clients/
│   └── ...
├── 03_Partners/
│   └── ...
├── 04_Marketing/
│   └── ...
├── 05_Product/
│   └── ...
├── 06_Knowledge_Base/
│   ├── gibLink_IP_Source/
│   │   ├── 00_Methodology_Core/
│   │   ├── 01_Strategy_Modules/
│   │   └── ... (full structure for the LM source)
│   ├── Competitor_Analysis.md
│   └── Swipe_File/
├── 07_Admin/
│   └── ...
├── 08_Processes/
│   ├── Ignition Sequence - Client Onboarding.md
│   └── MOC_Processes.md
└── Templates/
    └── ...
```

### Key Folder Explanations (Updated):

- **`02_Clients`**: A lightweight CRM. The actual _Blueprint deliverable_ lives in its own separate vault.
    
- **`06_Knowledge_Base`**: Now contains the **`gibLink_IP_Source`** folder. This is the new, secure home for the structured notes that will train your proprietary LM.
    
- **`08_Processes`**: A new section to document your standard operating procedures (SOPs). The **`Ignition Sequence - Client Onboarding.md`** note is the primary asset here, containing your checklists and questions for the Fluent System.
    

## 2. The Client Blueprint Template Vault Structure

This vault is your clean, master template. You will duplicate this entire folder structure for every new client engagement.

```
Client Blueprint Template Vault/
├── index.md
├── 01_Core_Identity/
│   ├── Brand Mission and Vision.md
│   └── ...
├── 02_Audience/
│   └── ...
├── 03_Content_Strategy/
│   ├── Content Pillars.md
│   └── SEO Strategy.md
├── 04_Content_Library/
│   ├── About_Us/
│   │   └── Company History.md
│   ├── Products/
│   │   └── Product A Description.md
│   ├── Services/
│   │   └── Service X Details.md
│   ├── Knowledge_Base/
│   │   └── How to do Task Y.md
│   └── MOC_Content_Library.md
├── 05_Campaigns/
│   └── Example Campaign Brief.md
├── 06_Performance_Log/
│   ├── 2025-Q4_Report.md
│   └── MOC_Performance_Log.md
└── Templates/
    └── TPL - New Campaign Brief.md
```

### Key Folder Explanations (Updated):

- **`index.md`**: This is the root file of the vault and will automatically serve as the home page when published as a web wiki for the client.
    
- **`04_Content_Library`**: This new section serves as the central repository for all canonical, client-approved content assets. It is the "single source of truth" for what the company says about itself, its products, and its services.
    

### The Workflow in Action:

1. **Onboard a New Client:** You sign "Client A."
    
2. **Run the Ignition Sequence:** You use the process documented in `08_Processes` to guide you through the "Fluent System" intake.
    
3. **Duplicate the Template:** Copy the entire `Client Blueprint Template Vault` and rename it to `Client A - Marketing Blueprint`.
    
4. **Populate the Blueprint:** Fill out the new vault with the client's information, placing all core content assets in the `04_Content_Library`.
    
5. **Share with Client:** You share the finished Blueprint with the client by publishing it as a private web wiki or by sharing the vault directly.
    

This refined structure provides a clear place for every piece of information and makes the deliverable far more practical for your clients.