# PleasantTools
Tools for Attacking Pleasant Password Server

https://www.mdsec.co.uk/2023/09/the-not-so-pleasant-password-manager/

## Simple Python decryptor

Query to find stored credential objects in MSSQL db:
```sql
SELECT Name,Notes,Username,Password FROM dbo.CredentialObject;
```

Decryption:
```bash
python3 decrypt.py                                                                                                
Usage: python decrypt.py username encrypted_password
```

