// Week 3 data: 29.06-05.07.2026
const week3Data = {
  period: "29.06-05.07.2026",
  week: 3,
  summary: {
    totalSpend: 91921.7,
    totalClicks: 1917,
    totalImpressions: 9000,
    avgCPC: 47.95,
    totalLeads: 45,
    cpl: 2042.7
  },
  direct: {
    msk: {
      campaigns: 19,
      spend: 47919.25,
      clicks: 1013,
      impressions: 5000
    },
    spb: {
      campaigns: 3,
      spend: 44002.45,
      clicks: 904,
      impressions: 4000
    }
  },
  webmaster: {
    msk: {
      impressions: 94164,
      clicks: 2350,
      ctr: 2.5
    },
    spb: {
      impressions: 46897,
      clicks: 1441,
      ctr: 3.07
    }
  },
  crm: {
    totalDeals: 125,
    targetLeads: 45,
    conversionRate: 36.0,
    byStage: {
      "КП направлено": 18,
      "Квалифицирован": 12,
      "Взято в работу": 10,
      "Передан на расчет": 2,
      "Встреча проведена": 2,
      "ДОГОВОР ПОДПИСАН": 1
    }
  }
};

// Export for use in dashboard
if (typeof module !== 'undefined' && module.exports) {
  module.exports = week3Data;
}
