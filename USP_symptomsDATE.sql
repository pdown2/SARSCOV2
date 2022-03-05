USE [COVSAR2]
GO

/****** Object:  StoredProcedure [dbo].[USP_symptomsDATE]    Script Date: 3/4/2022 3:46:39 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[USP_symptomsDATE]
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;




IF OBJECT_ID('dbo.STAMPsymptoms', 'U') IS NOT NULL 
	DROP TABLE dbo.STAMPsymptoms; 

IF OBJECT_ID('dbo.STAMPsymptomsDATE', 'U') IS NOT NULL 
	DROP TABLE dbo.STAMPsymptomsDATE; 

IF OBJECT_ID('dbo.STAMPsymptomsNODATE', 'U') IS NOT NULL 
	DROP TABLE dbo.STAMPsymptomsNODATE; 

SELECT subreddit, subreddit_id, author, body, created_utc, datetime, date, Address, sim0, sim1, sim2, sim3, 
	sim4, sim5, sim6, sim7, sim8, sim9, sim10, sim11, sim12, sim13, sim14, sim15, sim16, sim17, sim18, sim19, 
    sim20, sim21, sim22, sim23, sim24, sim25, sim26, sim27, sim28, sim29, sim30, sim31, sim32, sim33, sim34, 
	sim35, sim36, sim37, sim38, sim39, sim40

	  into STAMPsymptoms

  FROM [covsar2].[dbo].[symptoms_all_returns]

declare @id int, @sql nvarchar(max)

set @id = 1

while @id <= 40
	begin
		set @sql = 'IF OBJECT_ID(''dbo.STAMPsymptoms_Sim'+cast(@id as nvarchar(2))+''', ''U'') IS NOT NULL 
						DROP TABLE dbo.STAMPsymptoms_Sim'+cast(@id as nvarchar(2))+'; 

					SELECT subreddit, subreddit_id, author, body, created_utc, datetime, date, Address, sim'+cast(@id as nvarchar(2))+'

						into STAMPsymptoms_Sim'+cast(@id as nvarchar(2))+'
					  FROM [covsar2].[dbo].[symptoms_all_returns]

						Where isnull(sim'+cast(@id as nvarchar(2))+', 0) <> 0'

		exec (@sql)
		set @id = @id+1

	end
  
  delete 
  FROM [covsar2].[dbo].STAMPsymptoms
  where isnull(sim0+sim1+sim2+sim3+sim4+sim5+sim6+sim7+sim8+sim9+sim10+sim11+sim12+
      sim13+sim14+sim15+sim16+sim17+sim18+sim19+sim20+sim21+sim22+sim23+sim24+
      sim25+sim26+sim27+sim28+sim29+sim30+sim31+sim32+sim33+sim34+sim35+sim36+
      sim37+sim38+sim39+sim40, 0) = 0

select * into STAMPsymptomsNODATE from STAMPsymptoms where datetime is NULL

select * into STAMPsymptomsDATE from STAMPsymptoms where datetime is not NULL

END
GO


