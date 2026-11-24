# IBM Cognos Analytics — Dashboard Build Guide

## 1. Import the dataset
1. Sign in to your IBM Cognos Analytics workspace (a trial/account with Cognos Analytics access is required; an IBMid alone does not automatically provide a Cognos workspace).
2. Choose **New** → **Data** (or **Upload files**, depending on the workspace version).
3. Upload `Sales_Dataset.csv` and confirm that the first row contains column headers.
4. Check data types:
   - `Order Date`: Date
   - `Quantity`: Number / Integer
   - `Sales`, `Profit`: Number / Decimal
   - Remaining fields: String

## 2. Create the dashboard
1. Choose **New** → **Dashboard**.
2. Select the uploaded `Sales_Dataset` data source.
3. Add the following KPI visualizations. Use aggregation **Sum** or **Count** as indicated:
   - **Total Sales**: Sum of `Sales` (expected 468,017.67)
   - **Total Profit**: Sum of `Profit` (expected 131,342.54)
   - **Total Orders**: Count of `Order ID` (expected 240; distinct count is also 240)
   - **Units Sold**: Sum of `Quantity` (expected 1,552)

## 3. Add charts
- **Monthly Sales Trend**: Line chart; category/X-axis = `Order Date` (group by Month) or `Month`; measure/Y-axis = Sum of `Sales`. Sort months Jan–Dec.
- **Sales by Region**: Bar chart; category = `Region`; measure = Sum of `Sales`.
- **Sales Share by Category**: Pie or doughnut chart; category = `Category`; measure = Sum of `Sales`.

## 4. Add filters
Add interactive filters for:
- `Region`
- `Category`
- `Order Date`

## 5. Save and share
1. Save the dashboard with the title **Sales Performance Dashboard**.
2. If the assignment requires a shareable Cognos artifact, use Cognos **Share** / **Copy link** (subject to your account permissions).
3. Keep `Sales_Dataset.csv` and `Sales_Performance_Dashboard.xlsx` with the project files for GitHub submission.

## Validation
The imported dataset should produce these totals:

| KPI | Expected value |
|---|---:|
| Total Sales | 468,017.67 |
| Total Profit | 131,342.54 |
| Total Orders | 240 |
| Units Sold | 1,552 |

**Note:** The workbook's Dashboard sheet is an Excel preview/reference, not a native Cognos dashboard. The native dashboard must be created and saved inside an authenticated Cognos Analytics workspace.
