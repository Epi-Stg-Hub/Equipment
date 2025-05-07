using MudBlazor;
using MudBlazor.ThemeManager;

namespace BlazorApp2.Theme
{
    public static class CustomTheme
    {
        public static MudTheme MyCustomTheme = new MudTheme()
        {
            PaletteLight = new PaletteLight()
            {
                Primary = Colors.Green.Accent4,
                Secondary = Colors.Green.Accent4,
                Background = Colors.DeepOrange.Lighten5,
                AppbarBackground = "#1F1F1F",
                DrawerBackground = "#1F1F1F",
                Surface = "#1E1E2F",
                TextPrimary = "#ffffff",
            },
            PaletteDark = new PaletteDark()
            {
                Primary = Colors.Green.Accent4,
                Secondary = Colors.Green.Accent4,
                Background = Colors.DeepOrange.Lighten5,
                AppbarBackground = "#1F1F1F",
                DrawerBackground = "#1F1F1F",
                Surface = "#1E1E2F",
                TextPrimary = "#ffffff",
            },
            LayoutProperties = new LayoutProperties()
            {
                DefaultBorderRadius = "6px"
            },
        };
    }
}
