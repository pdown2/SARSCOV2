USE [COVSAR2]
GO

/****** Object:  StoredProcedure [dbo].[USP_symptomsDATE_Views]    Script Date: 3/4/2022 3:48:32 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[USP_symptomsDATE_Views]
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

declare @id int, @sql nvarchar(max)

set @id = 1
--'+cast(@id as nvarchar(2))+'


----drop views if present
----create views for all symptoms
while @id <= 40
	begin
		set @sql = 'Drop view  if exists dbo.VW_ProofofConcept_Date_Diffs_Sim'+cast(@id as nvarchar(2))
		exec (@sql)

		set @sql = 'CREATE VIEW VW_ProofofConcept_Date_Diffs_Sim'+cast(@id as nvarchar(2))+' AS
								SELECT S.author, S.datetime AS symptomsDATE, A.datetime AS authorDATE, 
										DATEDIFF(DAY, A.datetime, S.datetime) AS daysDifference
								FROM dbo.STAMPsymptoms_Sim'+cast(@id as nvarchar(2))+' AS S INNER JOIN
										 dbo.STAMPpositive AS A ON S.author = A.author'

		exec (@sql)
		set @id = @id+1

	end

END
GO


