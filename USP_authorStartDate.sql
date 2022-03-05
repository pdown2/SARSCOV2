USE [COVSAR2]
GO

/****** Object:  StoredProcedure [dbo].[USP_authorStartDate]    Script Date: 3/4/2022 3:44:53 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO


CREATE PROCEDURE [dbo].[USP_authorStartDate]

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	IF OBJECT_ID('dbo.STAMPpositive', 'U') IS NOT NULL 
	  DROP TABLE dbo.STAMPpositive; 

----remove duplicate authors by using the lowest date.
	SELECT T1.[author],   MIN(T2.[datetime]) as [datetime] into dbo.STAMPpositive
	FROM [wsb_comments] T1
		JOIN [wsb_comments] T2 ON T1.[author] = T2.[author]
		where t1.author   in (select author from author_valid)
	GROUP BY T1.[author]

END
GO


