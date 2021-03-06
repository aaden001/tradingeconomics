% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/worldBank.R
\name{getWorldBankCategories}
\alias{getWorldBankCategories}
\title{Get World Bank values from Trading Economics API}
\usage{
getWorldBankCategories(category = NULL, outType = NULL)
}
\arguments{
\item{category}{string.}

\item{outType}{string.
'df' for data frame,
'raw'(default) for list of unparsed data.}
}
\value{
Returns a list or data from World Bank.
}
\description{
Get World Bank values from Trading Economics API
}
\section{Notes}{

Without credentials only sample information will be provided. Without a category, a list of all categories will be provided.
}

\examples{
\dontrun{ getWorldBankCategories(outType = 'df')
getWorldBankCategories(category = 'education')
getWorldBankCategories(category = 'education')
}
}
\seealso{
\code{\link{getCalendarData}}, \code{\link{getForecastData}}, \code{\link{getHistoricalData}} and \code{\link{getIndicatorData}}
}
