# Farm Dashboard

This repository contains a basic React dashboard component. It displays dummy data for service alerts, snags, and monthly expenses using the Recharts library.

## Feature Suggestions
- **Supabase Integration**: Replace the dummy arrays with live data from a Supabase database. Set up tables for assets, service alerts, snags, and expenses.
- **Authentication**: Use Supabase Auth to allow farmers to log in and manage their own data.
- **CRUD Operations**: Provide forms to create and update assets, service schedules, and snags directly from the dashboard.
- **Notifications**: Add email or push notifications for upcoming service dates or overdue snags.
- **Enhanced Charts**: Display spending over time, asset usage statistics, and other metrics using additional chart types.

## Setup with Supabase
1. Create a Supabase project at [supabase.com](https://supabase.com/).
2. In the Supabase dashboard, set up tables for `assets`, `service_alerts`, `snags`, and `expenses`.
3. Obtain your project URL and anon API key from **Project Settings → API**.
4. Install the Supabase client:
   ```bash
   npm install @supabase/supabase-js
   ```
5. Initialize Supabase in your React app (e.g., in `src/lib/supabase.js`):
   ```javascript
   import { createClient } from '@supabase/supabase-js';
   const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL;
   const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
   export const supabase = createClient(supabaseUrl, supabaseKey);
   ```
6. Add `.env.local` with your Supabase credentials:
   ```bash
   NEXT_PUBLIC_SUPABASE_URL=your-project-url
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key
   ```
7. Fetch data in your component using `supabase.from('table').select()` and replace the dummy arrays.

## Deploy on Render
1. Push this repository to GitHub.
2. Create a new Web Service on [Render](https://render.com/) and connect it to your GitHub repository.
3. Set the build command to `npm install && npm run build` and the start command to `npm start` (or `npm run start` depending on your setup).
4. Add the environment variables from `.env.local` in the Render dashboard.
5. Deploy the service. Render will build your app and provide a URL.

