import { Component } from '@angular/core';
import {
  heroHome,
  heroBookOpen,
  heroCog6Tooth,
} from '@ng-icons/heroicons/outline';
import { NgIconComponent, provideIcons } from '@ng-icons/core';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [NgIconComponent, RouterModule],
  templateUrl: './sidebar.component.html',
  styleUrl: './sidebar.component.css',
  viewProviders: [provideIcons({ heroHome, heroBookOpen, heroCog6Tooth })],
})
export class SidebarComponent {}
