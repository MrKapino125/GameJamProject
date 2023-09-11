import card

class Cardloader:
    def loadcard(self, id, screen, eventhandler, timer):
        match id:
            case -1:
                return 36
            case 0:
                return card.ClickCard(screen, eventhandler, timer)
            case 1:
                return card.SliceCard(screen, eventhandler, timer)
            case 2:
                return card.MathCard(screen, eventhandler, timer)
            case 8:
                return card.RememberCard(screen, eventhandler, timer)
            case 3:
                return card.LabyrinthCard(screen, eventhandler, timer)
            case 10:
                return card.TriangleCard(screen, eventhandler, timer)
            case 9:
                return card.ImpossiblequizCard(screen, eventhandler, timer)
            case 4:
                return card.NotclickbuttonCard(screen, eventhandler, timer)
            case 7:
                return card.MessageCard(screen, eventhandler, timer)
            case 17:
                return card.RightCard(screen, eventhandler, timer)
            case 28:
                return card.MinefieldCard(screen, eventhandler, timer)
            case 27:
                return card.PressCard(screen, eventhandler, timer)
            case 26:
                return card.ColorCard(screen, eventhandler, timer)
            case 12:
                return card.AlphabetCard(screen, eventhandler, timer)
            case 18:
                return card.ReactionCard(screen, eventhandler, timer)
            case 15:
                return card.LightsCard(screen, eventhandler, timer)
            case 13:
                return card.ButtonsCard(screen, eventhandler, timer)
            case 24:
                return card.WingdingsCard(screen, eventhandler, timer)
            case 25:
                return card.ReplikaCard(screen, eventhandler, timer)
            case 22:
                return card.AsteroidsCard(screen, eventhandler, timer)
            case 19:
                return card.GraphCard(screen, eventhandler, timer)
            case 14:
                return card.PrimeCard(screen, eventhandler, timer)
            case 20:
                return card.PolygonCard(screen, eventhandler, timer)
            case 16:
                return card.TargetCard(screen, eventhandler, timer)
            case 6:
                return card.PasswordCard1(screen, eventhandler, timer)
            case 34:
                return card.PasswordCard2(screen, eventhandler, timer)
            case 21:
                return card.OrderCard(screen, eventhandler, timer)
            case 5:
                return card.TrailCard(screen, eventhandler, timer)
            case 11:
                return card.ColorwordCard(screen, eventhandler, timer)
            case 23:
                return card.MousebuttonsCard(screen, eventhandler, timer)
            case 32:
                return card.KeyboardpressCard(screen, eventhandler, timer)
            case 29:
                return card.CursorCard(screen, eventhandler, timer)
            case 33:
                return card.RacetrackCard(screen, eventhandler, timer)
            case 31:
                return card.CardnumberCard(screen, eventhandler, timer)
            case 30:
                return card.OsuCard(screen, eventhandler, timer)
            case 35:
                return card.WordleCard(screen, eventhandler, timer)
            case 36:
                return card.BallCard(screen, eventhandler, timer)