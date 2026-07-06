Database Versioning - Quick Explanation                                                           
                                                                                                    
  🎯 What is Database Versioning?                                                                   
                                                                                                    
  Instead of directly replacing your database when the source data changes, the new system:         
                                                                                                    
  1. Creates versioned snapshots - Each database has a version number (e.g., nse_equity_v1.0.0.db)  
  2. Uses symlinks for "current" - Your code uses nse_equity.db which points to                     
  versions/nse_equity_v1.0.0.db                                                                     
  3. Keeps old versions - Previous versions stay in versions/ folder for rollback                   
                                                                                                    
  🌟 Why This Matters                                                                               
                                                                                                    
  Before (Old Approach):                                                                            
                                                                                                    
  ❌ Update instruments.csv → Rebuild nse_equity.db → Hope nothing broke                            
  ❌ If data is bad, you've lost the old database                                                   
  ❌ Can't compare what changed                                                                     
  ❌ No approval process                                                                            
                                                                                                    
  After (New Approach):                                                                             
                                                                                                    
  ✅ Update instruments.csv → Build v1.1.0 in staging → Validate → Approve → Promote                
  ✅ Old v1.0.0 still available if v1.1.0 has issues                                                
  ✅ Can see exactly what changed between versions                                                  
  ✅ Quality gates before production                                                                
                                                                                                    
  🔄 The Complete Flow                                                                              
                                                                                                    
  1. Source Data (instruments.csv)                                                                  
           ↓                                                                                        
  2. Build Staging DB (v1.1.0) ← SQL filtering applied                                              
           ↓                                                                                        
  3. Validate ← Check data quality                                                                  
           ↓                                                                                        
  4. Review & Approve ← Manual verification                                                         
           ↓                                                                                        
  5. Promote to Production ← Symlink updated to v1.1.0                                              
           ↓                                                                                        
  6. Old v1.0.0 kept for rollback                                                                   
                                                                                                    
  ---                                                                                               
  📋 Commands You Need to Run                                                                       
                                                                                                    
  Scenario: NSE updated their instrument list                                                       
                                                                                                    
  # 1. BUILD: Create new version from updated CSV                                                   
  python scripts/db_builder.py \                                                                    
      --config data/staging/configs/instruments/nse_equity.yaml                                     
                                                                                                    
  # Output: Creates nse_equity_v1.1.0.db in staging/                                                
  # What it does: Reads instruments.csv, filters for NSE equity, creates v1.1.0                     
                                                                                                    
                                                                                                    
  # 2. VALIDATE: Check data quality                                                                 
  python scripts/db_validator.py \                                                                  
      --database data/staging/databases/instruments/nse_equity_v1.1.0.db                            
                                                                                                    
  # Output: ✓ VALIDATION PASSED (9,548 rows, all checks passed)                                     
  # What it does: Runs rules (row count, unique IDs, no duplicates)                                 
                                                                                                    
                                                                                                    
  # 3. REVIEW: See what's in the database                                                           
  python scripts/db_approver.py \                                                                   
      --database data/staging/databases/instruments/nse_equity_v1.1.0.db \                          
      --action review                                                                               
                                                                                                    
  # Output: Shows version, row count, filters applied, validation status                            
  # What it does: Displays summary for manual inspection                                            
                                                                                                    
                                                                                                    
  # 4. COMPARE: What changed from current version?                                                  
  python scripts/db_differ.py \                                                                     
      --old data/master/instruments/versions/nse_equity_v1.0.0.db \                                 
      --new data/staging/databases/instruments/nse_equity_v1.1.0.db                                 
                                                                                                    
  # Output: Rows added: 500, Rows deleted: 0, Rows modified: 0                                      
  # What it does: Shows exactly what changed between versions                                       
                                                                                                    
                                                                                                    
  # 5. APPROVE: Mark as ready for production                                                        
  python scripts/db_approver.py \                                                                   
      --database data/staging/databases/instruments/nse_equity_v1.1.0.db \                          
      --action approve \                                                                            
      --comment "500 new NSE listings added"                                                        
                                                                                                    
  # Output: ✓ Database approved successfully                                                        
  # What it does: Sets approval_status = 'approved' in metadata                                     
                                                                                                    
                                                                                                    
  # 6. PROMOTE: Make it the live production database                                                
  python scripts/db_promoter.py \                                                                   
      --database data/staging/databases/instruments/nse_equity_v1.1.0.db                            
                                                                                                    
  # Output: ✓ Database promoted successfully                                                        
  # What it does:                                                                                   
  #   - Copies to data/master/instruments/versions/nse_equity_v1.1.0.db                             
  #   - Updates symlink: nse_equity.db -> versions/nse_equity_v1.1.0.db                             
  #   - Keeps v1.0.0 in versions/ for rollback                                                      
                                                                                                    
  ---                                                                                               
  🔧 Version Management Commands                                                                    
                                                                                                    
  # LIST: See all versions available                                                                
  python scripts/db_version_manager.py --database nse_equity --action list                          
                                                                                                    
  # Output:                                                                                         
  #   1.1.0: 1,854,784 bytes, 9,548 rows (CURRENT)                                                  
  #   1.0.0: 1,654,784 bytes, 9,048 rows                                                            
                                                                                                    
                                                                                                    
  # ROLLBACK: Something wrong with v1.1.0? Go back!                                                 
  python scripts/db_version_manager.py --database nse_equity --action rollback                      
                                                                                                    
  # What it does: Updates symlink to point back to v1.0.0                                           
  # Your code still uses nse_equity.db - no changes needed!                                         
                                                                                                    
                                                                                                    
  # CLEANUP: Keep only last 5 versions                                                              
  python scripts/db_version_manager.py --database nse_equity --action cleanup --keep 5              
                                                                                                    
  # What it does: Deletes old versions, keeps newest 5                                              
                                                                                                    
  ---                                                                                               
  💡 Real-World Example                                                                             
                                                                                                    
  Your existing code doesn't change at all:                                                         
                                                                                                    
  # Your code (unchanged)                                                                           
  from kalkey.database.versioned_db import VersionedDB                                              
                                                                                                    
  with VersionedDB('nse_equity') as db_path:                                                        
      conn = sqlite3.connect(db_path)                                                               
      # Query database                                                                              
      conn.close()                                                                                  
                                                                                                    
  Behind the scenes:                                                                                
  - Uses nse_equity.db symlink                                                                      
  - Symlink points to current version (v1.1.0)                                                      
  - If you rollback, symlink points to v1.0.0                                                       
  - Your code never knows the difference!                                                           
                                                                                                    
  ---                                                                                               
  🎯 Key Benefits                                                                                   
  ┌─────────────────┬─────────────────────────────────────────────┐                                 
  │     Benefit     │                How It Helps                 │                                 
  ├─────────────────┼─────────────────────────────────────────────┤                                 
  │ Safety          │ Bad data? Rollback in 5 seconds             │                                 
  ├─────────────────┼─────────────────────────────────────────────┤                                 
  │ Traceability    │ Know exactly what changed and when          │                                 
  ├─────────────────┼─────────────────────────────────────────────┤                                 
  │ Quality         │ Validation catches issues before production │                                 
  ├─────────────────┼─────────────────────────────────────────────┤                                 
  │ Reproducibility │ Can query specific version for consistency  │                                 
  ├─────────────────┼─────────────────────────────────────────────┤                                 
  │ No Code Changes │ Existing code works unchanged               │                                 
  └─────────────────┴─────────────────────────────────────────────┘                                 
  ---                                                                                               
  🚀 Quick Start                                                                                    
                                                                                                    
  To update an existing database:                                                                   
                                                                                                    
  # 1. Edit the YAML config if needed (optional)                                                    
  # 2. Build new version                                                                            
  python scripts/db_builder.py --config data/staging/configs/instruments/nse_equity.yaml            
                                                                                                    
  # 3. Validate, approve, promote (3 commands)                                                      
  python scripts/db_validator.py --database data/staging/databases/instruments/nse_equity_v1.X.X.db 
  python scripts/db_approver.py --database data/staging/databases/instruments/nse_equity_v1.X.X.db  
  --action approve                                                                                  
  python scripts/db_promoter.py --database data/staging/databases/instruments/nse_equity_v1.X.X.db  
                                                                                                    
  That's it! Your production database is now updated with full rollback capability.                 
                                                  